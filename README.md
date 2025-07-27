# Python Package Cookiecutter Template

A comprehensive [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating modern Python packages with integrated tooling, best practices, and AI-assisted development support.

## 🎯 Features

This template generates Python packages with:

- 🏗️ **Modern Project Structure**: `src/` layout following current packaging standards
- 📦 **uv Integration**: Fast dependency management and virtual environment handling
- 🔧 **Code Quality Tools**: Pre-configured Black, Ruff, and pre-commit hooks
- 🧪 **Testing Setup**: pytest with coverage reporting and comprehensive test examples
- 📝 **Documentation Standards**: Google-style docstrings with examples throughout
- 🔄 **Semantic Versioning**: Commitizen for conventional commits and automated changelog
- ⚡ **Development Automation**: Makefile with common development tasks
- 🤖 **AI-Assisted Development**: GitHub Copilot instructions for consistent code generation
- 📄 **Multiple License Options**: MIT, Apache-2.0, BSD-3-Clause, GPL-3.0, BSD-2-Clause
- 🚀 **Production Ready**: Complete setup scripts and CI/CD preparation

## Quick Start

### Prerequisites

- Python 3.8+
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [uv](https://github.com/astral-sh/uv) package manager

### Install Cookiecutter

```bash
pip install cookiecutter
# or
pipx install cookiecutter
```

### Create a New Project

```bash
cookiecutter https://github.com/yourusername/python-package-cookiecutter
# or locally
cookiecutter /path/to/this/template
```

You'll be prompted for:

- **project_name**: The human-readable name (e.g., "My Awesome Package")
- **project_slug**: Auto-generated from project_name (e.g., "my_awesome_package")
- **package_name**: Python package name (auto-generated)
- **project_short_description**: Brief description of your package
- **author_name**: Your name
- **author_email**: Your email address
- **github_username**: Your GitHub username
- **github_url**: Auto-generated GitHub URL
- **version**: Initial version (default: "0.1.0")
- **license**: Choose from MIT, Apache-2.0, BSD-3-Clause, GPL-3.0, BSD-2-Clause
- **python_version**: Minimum Python version (default: "3.8")

### Example Generation

```bash
$ cookiecutter /path/to/template
project_name [My Python Package]: Data Processing Toolkit
project_slug [data_processing_toolkit]:
package_name [data_processing_toolkit]:
project_short_description [A short description of the package]: A toolkit for efficient data processing and analysis
author_name [Your Name]: John Doe
author_email [your.email@example.com]: john.doe@example.com
github_username [yourusername]: johndoe
github_url [https://github.com/johndoe/data_processing_toolkit]:
version [0.1.0]:
Select license:
1 - MIT
2 - Apache-2.0
3 - BSD-3-Clause
4 - GPL-3.0
5 - BSD-2-Clause
Choose from 1, 2, 3, 4, 5 [1]: 1
python_version [3.8]:
```

## 🔧 Template Structure

```
py-package/                                    # Cookiecutter Template Root
├── cookiecutter.json                         # Template configuration & variables
├── README.md                                  # This documentation
├── CHANGELOG.md                               # Template version history
├── test_template.sh                          # Template testing script
├── LICENSE                                    # Template license (MIT)
└── {{cookiecutter.project_slug}}/            # Generated Project Template
    ├── .github/
    │   └── copilot-instructions.md           # AI development guidelines
    ├── src/
    │   └── {{cookiecutter.package_name}}/
    │       ├── __init__.py                   # Package initialization
    │       └── core.py                       # Sample core functionality
    ├── tests/
    │   ├── __init__.py
    │   └── test_core.py                      # Comprehensive test examples
    ├── .pre-commit-config.yaml              # Pre-commit hooks config
    ├── pyproject.toml                        # Project configuration
    ├── README.md                             # Generated project docs
    ├── Makefile                              # Development automation
    ├── setup.sh                             # Environment setup script
    ├── CHANGELOG.md                          # Project changelog
    ├── LICENSE                               # Selected license file
    └── .gitignore                            # Python gitignore
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter): `pip install cookiecutter`
- [uv](https://github.com/astral-sh/uv): Fast Python package manager

### Generate Your Project

```bash
# From GitHub (when published)
cookiecutter gh:yourusername/python-package-cookiecutter

# From local template
cookiecutter /path/to/this/template

# Non-interactive with custom values
cookiecutter /path/to/template --no-input \
    project_name="My Awesome Package" \
    author_name="Your Name" \
    author_email="you@example.com"
```

### Customization Variables

You'll be prompted to customize:

| Variable | Description | Example |
|----------|-------------|---------|
| `project_name` | Human-readable project name | "Data Science Toolkit" |
| `project_slug` | URL-friendly name (auto-generated) | "data_science_toolkit" |
| `package_name` | Python package name (auto-generated) | "data_science_toolkit" |
| `project_short_description` | Brief project description | "A toolkit for data analysis" |
| `author_name` | Your full name | "Jane Smith" |
| `author_email` | Your email address | "jane@example.com" |
| `github_username` | GitHub username | "janesmith" |
| `github_url` | Repository URL (auto-generated) | "https://github.com/janesmith/..." |
| `version` | Initial version | "0.1.0" |
| `license` | License choice | MIT, Apache-2.0, BSD-3-Clause, etc. |
| `python_version` | Minimum Python version | "3.8" |

### Example Generation Session

```bash
$ cookiecutter /path/to/template

project_name [My Python Package]: Data Science Toolkit
project_slug [data_science_toolkit]:
package_name [data_science_toolkit]:
project_short_description [A short description of the package]: Comprehensive data analysis and visualization toolkit
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane.smith@datascience.com
github_username [yourusername]: janesmith
github_url [https://github.com/janesmith/data_science_toolkit]:
version [0.1.0]:
Select license:
1 - MIT
2 - Apache-2.0
3 - BSD-3-Clause
4 - GPL-3.0
5 - BSD-2-Clause
Choose from 1, 2, 3, 4, 5 [1]: 1
python_version [3.8]: 3.9
```

## 📦 Generated Project Features

### Development Workflow

After generation, your project includes:

1. **Immediate Setup:**
   ```bash
   cd your_generated_project
   ./setup.sh  # Complete environment setup
   ```

2. **Development Commands:**
   ```bash
   make test     # Run comprehensive tests
   make lint     # Code quality checks
   make format   # Auto-format code
   cz commit     # Conventional commits
   make release  # Semantic version bump
   ```

### Included Sample Code

The template provides working examples:

- **Calculator Class**: Demonstrates OOP patterns, type hints, and history tracking
- **Greet Function**: Shows simple function design with optional parameters
- **Comprehensive Tests**: Full pytest suite with fixtures, parametrization, and edge cases
- **Google-Style Docstrings**: Complete documentation examples with Args, Returns, Examples
- **Error Handling**: Proper exception handling and validation patterns

### Development Tools Integration

- **Black**: Code formatting (88-character line length)
- **Ruff**: Fast linting with auto-fixes and import sorting
- **pytest**: Testing framework with coverage reporting
- **Pre-commit**: Automated quality checks on git commit
- **Commitizen**: Semantic versioning and changelog generation
- **uv**: Fast dependency management and virtual environments

## 🤖 AI-Assisted Development

Each generated project includes comprehensive GitHub Copilot instructions:

- **Code Generation Guidelines**: Consistent patterns and conventions
- **Documentation Standards**: Google-style docstring examples
- **Testing Patterns**: pytest best practices and structure
- **Quality Standards**: Linting rules and formatting expectations
- **Project Context**: Understanding of the package architecture

This ensures AI assistance follows your project's established patterns and maintains high code quality.

## 🎯 Complete Workflow Example

Here's a complete example of using this template to create a new project:

### Step 1: Generate Your Project

```bash
$ cookiecutter /Users/duy/repos/py-package

project_name [My Python Package]: Weather Data Processor
project_slug [weather_data_processor]:
package_name [weather_data_processor]:
project_short_description [A short description of the package]: A Python library for processing and analyzing weather data
author_name [Your Name]: Alex Johnson
author_email [your.email@example.com]: alex.johnson@weather.com
github_username [yourusername]: alexjohnson
github_url [https://github.com/alexjohnson/weather_data_processor]:
version [0.1.0]:
Select license:
1 - MIT
2 - Apache-2.0
3 - BSD-3-Clause
4 - GPL-3.0
5 - BSD-2-Clause
Choose from 1, 2, 3, 4, 5 [1]: 1
python_version [3.8]: 3.9
```

### Step 2: Set Up Development Environment

```bash
cd weather_data_processor
./setup.sh
# OR manually:
# uv venv && source .venv/bin/activate
# uv pip install -e ".[dev]"
# pre-commit install && pre-commit install --hook-type commit-msg
```

### Step 3: Start Developing

```bash
# Run tests to verify everything works
make test

# Check code quality
make lint

# Start coding your features in src/weather_data_processor/
# Add tests in tests/
# Use conventional commits
cz commit
```

### Step 4: What You Get

Your generated project includes:

- **Ready-to-use package structure** with example Calculator and greet functions
- **Complete test suite** with 15+ test cases showing best practices
- **Quality tooling** configured and working (Black, Ruff, pytest, pre-commit)
- **Documentation templates** with Google-style docstrings
- **CI/CD ready** structure for GitHub Actions
- **Semantic versioning** setup with automated changelog
- **GitHub Copilot instructions** for consistent AI-assisted development

## 🧪 Testing the Template

The template includes a comprehensive test script that validates the entire workflow:

```bash
# Make the script executable (if not already)
chmod +x test_template.sh

# Run the complete test suite
./test_template.sh
```

### What the Test Script Does

The `test_template.sh` script performs a complete end-to-end validation:

1. **Environment Verification**: Checks for required tools (cookiecutter, uv)
2. **Template Generation**: Creates a test project with default values:
   - Project name: "Test Package"
   - Author: "Test Author"
   - Email: "test@example.com"
   - GitHub username: "testuser"
3. **Development Setup**:
   - Creates virtual environment with `uv venv`
   - Installs all dependencies including dev tools
   - Sets up pre-commit hooks
4. **Quality Validation**:
   - Runs complete test suite with `pytest`
   - Validates code formatting with `black --check`
   - Performs linting with `ruff check`
   - Tests all Makefile targets
5. **Cleanup Information**: Provides commands to remove test artifacts

### Test Output Example

```bash
🧪 Testing Cookiecutter Python Package Template
==============================================
📁 Testing in: /tmp/cookiecutter-test-1234567890
🏗️  Generating test project...
📦 Setting up test project environment...
🧪 Running tests...
========================== test session starts ===========================
collected 15 items

tests/test_core.py ............... [100%]

========================== 15 passed in 0.12s ==========================
🔧 Running linting...
All done! ✨ 🍰 ✨
All done! ✨ 🍰 ✨
📋 Running make targets...
✅ Cookiecutter template test completed successfully!
```

This ensures every generated project works perfectly out of the box!

## 🔧 Template Customization

### Adding New Variables

1. **Update `cookiecutter.json`:**
   ```json
   {
       "new_variable": "default_value",
       "choice_variable": ["option1", "option2", "option3"]
   }
   ```

2. **Use in template files:**
   ```
   {{ cookiecutter.new_variable }}
   ```

### Modifying Generated Content

- Edit files in `{{cookiecutter.project_slug}}/`
- Use Jinja2 templating for dynamic content
- Test changes with `./test_template.sh`

## 📋 What Makes This Template Special

1. **Production Ready**: Generated projects are immediately ready for development and deployment
2. **Modern Standards**: Follows current Python packaging best practices (PEP 517/518, src/ layout)
3. **Quality First**: Built-in testing, linting, and documentation requirements
4. **AI-Enhanced**: GitHub Copilot integration for consistent development experience
5. **Flexible Licensing**: Support for multiple open-source licenses
6. **Developer Experience**: Comprehensive automation and clear development workflows
7. **Extensible**: Easy to customize for specific organizational needs

## 🤝 Contributing to the Template

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-improvement`)
3. Make your changes to the template
4. Test with `./test_template.sh`
5. Update documentation as needed
6. Commit using conventional commits (`cz commit`)
7. Open a Pull Request

## 📄 License

This Cookiecutter template is licensed under the MIT License. Generated projects use the license selected during template generation.

## 🎉 Summary

This Cookiecutter template provides everything you need to create production-ready Python packages:

**🚀 For Package Authors:**
- Start with a complete, working package structure
- Modern tooling configured and ready to use
- Comprehensive examples and documentation
- AI-assisted development with GitHub Copilot integration

**🔧 For Development Teams:**
- Consistent project structure across all packages
- Enforced code quality and testing standards
- Automated workflows and semantic versioning
- Easy customization for organizational needs

**📦 For the Python Community:**
- Follows current packaging best practices (PEP 517/518, src/ layout)
- Includes comprehensive testing and documentation examples
- Promotes quality code with integrated tooling
- Supports multiple open-source licenses

---

**Ready to create your next Python package?** Just run:

```bash
cookiecutter /path/to/this/template
```

And start building something amazing! 🚀
- 📝 **Documentation**: Google-style docstrings throughout
- 🔄 **Semantic Versioning**: Commitizen for conventional commits and automated changelog
- ⚡ **Development Automation**: Makefile for common development tasks

## Quick Start

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd my-python-package
   ```

2. **Set up development environment:**
   ```bash
   # Create virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev]"
   ```

3. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   pre-commit install --hook-type commit-msg
   ```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=my_python_package --cov-report=html

# Run specific test file
pytest tests/test_core.py
```

### Code Quality

```bash
# Format code
black src tests

# Lint code
ruff check src tests

# Run all quality checks
make lint
```

### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards

3. **Commit using conventional commits:**
   ```bash
   git add .
   cz commit  # Interactive commit message helper
   # or manually: git commit -m "feat: add new feature"
   ```

4. **Push and create a pull request**

### Available Make Commands

```bash
make help          # Show available commands
make install       # Install package in development mode
make test          # Run tests
make lint          # Run all linting and formatting
make clean         # Clean build artifacts
make docs          # Generate documentation (if configured)
make release       # Create a new release with commitizen
```

## Package Usage

```python
from my_python_package import Calculator, greet

# Simple greeting
message = greet("World")
print(message)  # "Hello, World!"

# Use the calculator
calc = Calculator()
result = calc.add(10, 5)
print(f"10 + 5 = {result}")

# Check calculation history
history = calc.get_history()
print(f"Operations performed: {len(history)}")
```

## Project Structure

```
my-python-package/
├── .github/
│   └── copilot-instructions.md  # GitHub Copilot development guidelines
├── src/
│   └── my_python_package/
│       ├── __init__.py          # Package initialization
│       └── core.py              # Core functionality
├── tests/
│   ├── __init__.py
│   └── test_core.py             # Unit tests
├── .pre-commit-config.yaml      # Pre-commit hooks configuration
├── pyproject.toml               # Project configuration and dependencies
├── README.md                    # This file
├── Makefile                     # Development automation
└── CHANGELOG.md                 # Auto-generated changelog
```

## Configuration

All tool configurations are centralized in `pyproject.toml`:

- **Black**: Code formatting (88 character line length)
- **Ruff**: Fast linting with sensible defaults
- **pytest**: Test discovery and coverage reporting
- **Commitizen**: Conventional commits and semantic versioning

## AI-Assisted Development

This project includes GitHub Copilot instructions to help with AI-assisted development:

- **Copilot Instructions**: See `.github/copilot-instructions.md` for detailed guidelines
- **Code Standards**: AI assistance follows project's coding standards and practices
- **Documentation**: Copilot understands the Google-style docstring requirements
- **Testing**: AI can help generate tests following the established patterns

The instructions help ensure consistent code generation that matches the project's architecture and quality standards.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the code style (see `.github/copilot-instructions.md` for details)
4. Add tests for new functionality
5. Commit your changes using conventional commits (`cz commit`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes to this project.
