# Prompty Getting Started with OpenAI

This repository demonstrates how to use Microsoft Prompty with OpenAI API. The setup includes environment variable management to keep your API keys secure and works great in VS Code DevContainers.

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the template file and add your OpenAI API key:

```bash
cp .env.template .env
```

Edit `.env` and replace `your_openai_api_key_here` with your actual OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Get Your OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in to your account
3. Create a new API key
4. Copy the key to your `.env` file

### 4. Test Your Setup

```bash
python test_prompty.py
```

## 📁 File Structure

- `basic.prompty` - Main prompty template configured for OpenAI
- `.env.template` - Template for environment variables (safe to commit)
- `.env` - Your actual environment variables (DO NOT COMMIT)
- `test_prompty.py` - Test script to verify your setup
- `requirements.txt` - Python dependencies
- `.gitignore` - Ensures secrets aren't committed

## 🔧 Configuration Details

The `basic.prompty` file is configured to use OpenAI's API:

```yaml
model:
  api: chat
  configuration:
    type: openai
    name: gpt-4o-mini
  parameters:
    max_tokens: 3000
```

The OpenAI API key is automatically loaded from the `OPENAI_API_KEY` environment variable by the prompty runtime.

## 🛡️ Security

- ✅ `.env` is in `.gitignore` - your secrets won't be committed
- ✅ `.env.template` provides a safe template for sharing
- ✅ API keys are loaded from environment variables

## � Usage Examples

### Using the Prompty CLI

```bash
prompty -s basic.prompty
```

### Using in Python Code

```python
import prompty
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Execute the prompty
result = prompty.execute(
    "basic.prompty",
    inputs={
        "firstName": "Alice",
        "context": "Your context here...",
        "question": "Your question here..."
    }
)

print(result)
```

## 🔍 Troubleshooting

### Error: Invalid API Key
- Ensure your `.env` file has the correct `OPENAI_API_KEY`
- Verify the API key is valid at [OpenAI Platform](https://platform.openai.com/api-keys)

### Module Not Found Errors
- Install dependencies: `pip install -r requirements.txt`

### Prompty Not Found
- Make sure you're running commands from the repository root directory
- Verify `basic.prompty` exists in the current directory

## 📚 Learn More

- [Microsoft Prompty Documentation](https://github.com/microsoft/prompty)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Prompty Specification](https://github.com/microsoft/prompty/blob/main/web/docs/prompty-specification/page.mdx)

### Setup

1. **Clone and Open in DevContainer**
   ```bash
   git clone <your-repo-url>
   cd prompty-gs
   ```
   
2. **Open in VS Code**
   ```bash
   code .
   ```

3. **Reopen in Container**
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Dev Containers: Reopen in Container"
   - Wait for the container to build and start

4. **Configure Environment**
   ```bash
   cp .env.template .env
   ```
   Edit `.env` with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   **Note**: The Context7 API key will be prompted by VS Code when the MCP server starts for the first time and stored securely.

## 🛠 What's Included

### DevContainer Features
- **Python 3.11** development environment
- **Node.js LTS** for MCP server support
- **Git** and **GitHub CLI** pre-installed
- **VS Code Extensions**:
  - Python language support
  - Jupyter notebooks
  - Code formatting (Black, isort)
  - Linting (Flake8, Ruff)
  - JSON support

### Python Packages
- `prompty` - Core Prompty framework
- `openai` - OpenAI API client
- `azure-openai` - Azure OpenAI support
- `python-dotenv` - Environment variable management
- `jupyter` - Jupyter notebook support
- Development tools: `black`, `flake8`, `isort`, `pytest`

### Context7 MCP Server
- **Native VS Code Integration** - MCP servers are configured directly in the devcontainer
- **Automatic Setup** - VS Code handles MCP server configuration and startup
- **Secure API Key Management** - VS Code prompts for API keys and stores them securely
- **File System Access** - Includes filesystem MCP server for workspace operations

## 🏃‍♂️ Running the Examples

### Check Configuration Status
```bash
python src/main.py
```

### Run Prompty Example
```bash
python examples/prompty_example.py
```

### Run Tests
```bash
pytest tests/ -v
```

### Debug in VS Code
1. Open any Python file
2. Press `F5` or use the Debug panel
3. Choose "Python: Current File" configuration

### Using MCP Servers in Agent Mode
1. Open the Chat view (`Ctrl+Cmd+I` on Mac, `Ctrl+Alt+I` on Windows/Linux)
2. Select "Agent mode" from the dropdown
3. Click the "Tools" button to see available MCP tools
4. Start chatting - tools will be automatically invoked as needed

**Available Tools**:
- **Context7**: Context management, memory storage, workflow orchestration
- **Filesystem**: File operations, directory browsing, file content analysis

## 🔧 Configuration

### Environment Variables
Create a `.env` file from the template:
```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Azure OpenAI Configuration (alternative)
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Other settings
DEBUG=false
LOG_LEVEL=INFO
```

### MCP Server Configuration
MCP servers are automatically configured by VS Code through the devcontainer. The configuration includes:

**Context7 MCP Server**:
- VS Code will prompt for the API key on first use
- Provides context management and AI workflow tools

**Filesystem MCP Server**:
- Pre-configured for workspace access
- Enables file operations through agent mode

You can view and manage MCP servers in VS Code:
1. Open the Extensions view (`Ctrl+Shift+X`)
2. Look for the "MCP SERVERS - INSTALLED" section
3. Use the Command Palette: "MCP: List Servers"

## 📝 Creating Prompty Files

Prompty files use YAML frontmatter with template content:

```yaml
---
name: My Prompt
description: A sample prompt
model:
  api: chat
  configuration:
    type: openai
    api_key: ${env:OPENAI_API_KEY}
  parameters:
    model: gpt-4
    max_tokens: 1000
    temperature: 0.7
sample:
  user_input: "Hello world"
---

# System
You are a helpful assistant.

# User
{{user_input}}
```

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_main.py -v
```

## 🐛 Debugging

### VS Code Debugging
- Set breakpoints in your Python code
- Press `F5` to start debugging
- Use the integrated terminal for interactive debugging

### MCP Server Debugging
- Check MCP server status in the Extensions view
- Use "MCP: Show Output" to view server logs
- Restart servers via "MCP: List Servers" command

## 📚 Next Steps

1. **Explore Prompty**: Check out the [official documentation](https://github.com/microsoft/prompty)
2. **Context7 Integration**: Learn more about MCP servers
3. **Build Your App**: Start creating your own Prompty templates
4. **Add Dependencies**: Install additional packages as needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter issues:
1. Check that Docker is running
2. Verify all environment variables are set
3. Rebuild the DevContainer if needed
4. Check the setup script logs
