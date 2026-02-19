# Project Overview

Very simple test of Claude's ability to write python scripts.

## Tech Stack

<!-- List primary languages, frameworks, libraries, and tools -->
- Python:
- setuptools:
- pip:
- sqllite:
- pytest:

## Project Structure

<!-- Key directories and what they contain -->
```
/
├── src/        #
├── tests/      #
└── ...
```

## Development Setup

<!-- Commands to get the project running locally -->
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/Scripts/activate  # Windows (bash)
# .venv\Scripts\activate       # Windows (cmd/PowerShell)

# Install dependencies
pip install setuptools pytest

# Install package in editable mode
pip install -e .

# Run tests
pytest
```

## Common Commands

<!-- Frequently used commands Claude should know about -->
| Command | Description |
|---------|-------------|
| `source .venv/Scripts/activate` | Activate virtual environment (bash) |
| `pip install setuptools pytest` | Install dependencies |
| `pytest` | Run all tests |
| `pytest tests/test_foo.py` | Run a specific test file |
| `pip freeze > requirements.txt` | Export installed packages |
| `pip install -e .` | Install package in editable mode |

## Code Conventions

<!-- Style rules, naming conventions, patterns to follow -->
- **Formatting**: <!-- e.g., Prettier, Black, gofmt — enforced by CI? -->
- **Naming**: <!-- e.g., camelCase for variables, PascalCase for components -->
- **File structure**: <!-- e.g., one component per file, colocate tests -->
- **Imports**: <!-- e.g., absolute imports from src/, no barrel files -->

## Architecture Notes

<!-- Key architectural decisions, patterns in use, things to be aware of -->

## Testing

<!-- How tests are organized, what to test, how to run subsets -->

## Environment Variables

<!-- List required env vars and where to find/set them — no secrets here -->
```
VAR_NAME=     # Description
```

## Gotchas & Known Issues

<!-- Things that are non-obvious or have caused confusion before -->

## Out of Scope

<!-- Anything Claude should NOT do or change in this codebase -->
