#!/usr/bin/env python3
import pandas as pd
import os
from datetime import datetime

def extract_t12_to_csv():
    excel_file = 'Sample_T12.xlsx'
    csv_file = 't12_data.csv'
    prompty_file = 't12.prompty'
    
    print(f"Reading Excel file: {excel_file}")
    
    try:
        xls = pd.ExcelFile(excel_file)
        
        all_data = []
        
        for sheet_name in xls.sheet_names:
            print(f"Processing sheet: {sheet_name}")
            df = pd.read_excel(xls, sheet_name=sheet_name)
            
            if len(xls.sheet_names) > 1:
                all_data.append(f"=== Sheet: {sheet_name} ===")
            
            csv_string = df.to_csv(index=False)
            all_data.append(csv_string)
        
        csv_content = '\n'.join(all_data)
        
        print(f"Writing CSV file: {csv_file}")
        with open(csv_file, 'w') as f:
            f.write(csv_content)
        
        print(f"Updating prompty file: {prompty_file}")
        with open(prompty_file, 'r') as f:
            prompty_content = f.read()
        
        if '{{document}}' in prompty_content:
            updated_content = prompty_content.replace('{{document}}', csv_content)
        else:
            lines = prompty_content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('Process this T12 document:'):
                    lines[i] = f'Process this T12 document:\n\n{csv_content}'
                    break
            updated_content = '\n'.join(lines)
        
        with open(prompty_file, 'w') as f:
            f.write(updated_content)
        
        print(f"Successfully extracted data at {datetime.now().isoformat()}")
        print(f"- CSV file saved: {csv_file}")
        print(f"- Prompty file updated: {prompty_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    extract_t12_to_csv()