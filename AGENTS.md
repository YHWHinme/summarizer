# Agent Guidelines for Video Summarizer

## Build & Test Commands
- **Install dependencies**: `uv pip install -e .` or `pip install -e .`
- **Build package**: `uv build` or `python -m build`
- **Run installation test**: `python test_installation.py`
- **Run single test**: No formal test framework; use `python test_installation.py` for dependency checks

## Code Style Guidelines

### Imports
- Standard library imports first, then third-party, then local
- Use absolute imports
- Group imports by category with blank lines

### Formatting
- Use 4 spaces for indentation
- Line length: 100 characters max
- Use f-strings for string formatting
- Use pathlib.Path for file operations

### Types & Naming
- Use type hints for function parameters and return values
- snake_case for variables, functions, and methods
- PascalCase for classes
- UPPER_CASE for constants

### Error Handling
- Use try/except blocks with specific exception types
- Provide meaningful error messages
- Use click.echo for CLI error output

### File Operations
- Always use UTF-8 encoding
- Use context managers (with statements)
- Validate file existence before operations
- Use json.dump with indent=2 for pretty printing

### Documentation
- Use docstrings for all public functions and classes
- Include parameter descriptions and return types
- Keep docstrings concise but informative

### CLI Patterns
- Use Click decorators for command-line interfaces
- Validate file paths with click.Path(exists=True)
- Use required=True for mandatory options
- Handle exceptions gracefully in main functions