#!/usr/bin/env python3
import pandas as pd
import os
from datetime import datetime

def extract_t12_to_csv():
    excel_file = 'Sample_T12.xlsx'
    csv_file = 't12_data.csv'
    
    print(f"Reading Excel file: {excel_file}")
    
    try:
        xls = pd.ExcelFile(excel_file)
        
        for sheet_name in xls.sheet_names:
            print(f"Processing sheet: {sheet_name}")
            df = pd.read_excel(xls, sheet_name=sheet_name)
            
            # Find the proper header row (contains "Code", "Category", "Line Item")
            header_row_idx = None
            for i, row in df.iterrows():
                if (str(row.iloc[0]).strip() == 'Code' and 
                    str(row.iloc[1]).strip() == 'Category' and 
                    str(row.iloc[2]).strip() == 'Line Item'):
                    header_row_idx = i
                    break
            
            if header_row_idx is None:
                print("Warning: Could not find proper header row, using default")
                header_row_idx = 1
            
            # Extract the header row to preserve the actual column names
            header_row = df.iloc[header_row_idx].copy()
            
            # Convert date columns to readable format in header
            for i in range(3, len(header_row)):
                if pd.notna(header_row.iloc[i]):
                    try:
                        if hasattr(header_row.iloc[i], 'strftime'):
                            header_row.iloc[i] = header_row.iloc[i].strftime('%Y-%m')
                        else:
                            header_row.iloc[i] = str(header_row.iloc[i])
                    except:
                        header_row.iloc[i] = f"Month_{i-2}"
            
            # Create a copy of df for processing (don't modify original dates)
            df_work = df.copy()
            
            # Convert monthly columns to numeric for filtering (skip header row)
            monthly_cols = df_work.columns[3:]
            for col in monthly_cols:
                df_work[col] = pd.to_numeric(df_work[col], errors='coerce').fillna(0)
            
            # Create masks for filtering data rows (exclude header row from filtering)
            non_header_mask = df_work.index != header_row_idx
            
            # 1. Has actual monthly data (not all zeros)
            has_monthly_data = df_work[monthly_cols].abs().sum(axis=1) > 0
            
            # 2. Has meaningful category/line item
            has_category = df_work.iloc[:, 1].notna() & (df_work.iloc[:, 1].astype(str).str.strip() != '')
            has_line_item = df_work.iloc[:, 2].notna() & (df_work.iloc[:, 2].astype(str).str.strip() != '')
            
            # 3. Filter out section headers and total lines
            line_item_str = df_work.iloc[:, 2].astype(str).str.lower()
            is_not_section = ~line_item_str.str.contains(
                'total|income|expense|controllable|administration|marketing|salaries|contract|'
                'maintenance|turnover|utilities|interest|insurance|management|capital|special|'
                'debt service|rubs|^monthly$', 
                case=False, na=False
            )
            
            # 4. Filter out other header-like rows
            category_str = df_work.iloc[:, 1].astype(str).str.lower()
            is_not_other_header = ~category_str.str.contains(
                '^monthly$|^unnamed', case=False, na=False
            )
            
            # Combine filters for data rows (only apply to non-header rows)
            data_mask = (non_header_mask & has_monthly_data & has_category & 
                        has_line_item & is_not_section & is_not_other_header)
            
            # Keep header row and valid data rows
            final_mask = (df_work.index == header_row_idx) | data_mask
            
            filtered_df = df_work[final_mask]
            
            # Replace the header row with our formatted version
            filtered_df.iloc[0] = header_row
            
            print(f"Original rows: {len(df)}, Filtered rows: {len(filtered_df)}")
            
            print(f"Writing CSV file: {csv_file}")
            filtered_df.to_csv(csv_file, index=False)
        
        print(f"Successfully extracted data at {datetime.now().isoformat()}")
        print(f"- CSV file saved: {csv_file}")
        print("- Removed rows without monthly data or section headers")
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    extract_t12_to_csv()