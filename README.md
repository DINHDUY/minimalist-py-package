# Python Package Cookiecutter Template

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating modern Python packages with best practices and integrated tooling.

## What You Get

This template generates Python packages with:

- Modern `src/` layout structure
- Pre-configured development tools (Black, Ruff, pytest)
- Comprehensive testing setup with examples
- Google-style docstrings and documentation
- Automated development workflow with Make commands
- GitHub Copilot integration for AI-assisted development

## Quick Start

### 1. Install Prerequisites

```bash
# Install cookiecutter
pip install cookiecutter

# Install uv (recommended package manager)
pip install uv
```

### 2. Create Your Package

```bash
# Use this template locally
cookiecutter /path/to/this/template

# Or from GitHub (when published)
cookiecutter gh:yourusername/python-package-cookiecutter
```

### 3. Configure Your Package

You'll be prompted for these details:

| Field | Description | Example |
|-------|-------------|---------|
| `project_name` | Human-readable project name | "Data Processing Toolkit" |
| `project_slug` | URL-friendly name (auto-generated) | "data_processing_toolkit" |
| `package_name` | Python package name (auto-generated) | "data_processing_toolkit" |
| `project_short_description` | Brief description | "A toolkit for data processing" |
| `author_name` | Your full name | "John Doe" |
| `author_email` | Your email | "john@example.com" |
| `github_username` | GitHub username | "johndoe" |
| `version` | Initial version | "0.1.0" |
| `license` | License choice | MIT, Apache-2.0, BSD-3-Clause, etc. |
| `python_version` | Minimum Python version | "3.8" |

### 4. Set Up Development Environment

```bash
cd your_new_package
./setup.sh  # Automated setup
```

Or manually:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
pre-commit install
```

### 5. Start Developing

```bash
make test     # Run tests
make lint     # Check code quality
make format   # Format code
cz commit     # Use conventional commits
```

## Example Session

```bash
$ cookiecutter /path/to/template

project_name [My Python Package]: Weather API Client
project_slug [weather_api_client]:
package_name [weather_api_client]:
project_short_description [A short description of the package]: A Python client for weather data APIs
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane@example.com
github_username [yourusername]: janesmith
github_url [https://github.com/janesmith/weather_api_client]:
version [0.1.0]:
Select license:
1 - MIT
2 - Apache-2.0
3 - BSD-3-Clause
4 - GPL-3.0
5 - BSD-2-Clause
Choose from 1, 2, 3, 4, 5 [1]: 1
python_version [3.8]:

$ cd weather_api_client
$ ./setup.sh
$ make test
========================== 15 passed in 0.12s ==========================
```

## Generated Project Structure

```
your_package/
├── src/
│   └── your_package/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── Makefile
├── setup.sh
└── README.md
    ```

## Testing the Template

Run the included test script to verify everything works:

```bash
chmod +x test_template.sh
./test_template.sh
```

This creates a test project, installs dependencies, runs tests, and validates the complete workflow.


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
