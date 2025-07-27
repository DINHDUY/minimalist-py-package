#!/bin/bash
# Test script for the Cookiecutter template

set -e

echo "🧪 Testing Cookiecutter Python Package Template"
echo "=============================================="

# Check if cookiecutter is installed
if ! command -v cookiecutter &> /dev/null; then
    echo "❌ cookiecutter is not installed. Installing..."
    pip install cookiecutter
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Create a temporary directory for testing
TEST_DIR="/tmp/cookiecutter-test-$(date +%s)"
mkdir -p "$TEST_DIR"
cd "$TEST_DIR"

echo "📁 Testing in: $TEST_DIR"

# Generate project with default values (non-interactive)
echo "🏗️  Generating test project..."
cookiecutter --no-input "$(dirname "$0")" \
    project_name="Test Package" \
    author_name="Test Author" \
    author_email="test@example.com" \
    github_username="testuser" \
    project_short_description="A test package generated from cookiecutter template"

# Navigate to generated project
cd test_package

echo "📦 Setting up test project environment..."

# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
pre-commit install --hook-type commit-msg

echo "🧪 Running tests..."
pytest

echo "🔧 Running linting..."
black --check src tests
ruff check src tests

echo "📋 Running make targets..."
make help
make test
make lint

echo ""
echo "✅ Cookiecutter template test completed successfully!"
echo "📁 Test project created at: $TEST_DIR/test_package"
echo ""
echo "To clean up:"
echo "   rm -rf $TEST_DIR"
echo ""
