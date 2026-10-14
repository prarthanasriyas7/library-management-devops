
# Library Management System — DevOps Practicum

A Python Library Management System module used to demonstrate
Continuous Integration using GitHub Actions.

## Features

- Add books
- Search by book ID, title, or author
- Issue and return books
- Delete books
- View total, available, and issued counts
- Automated testing using Python unittest
- CI workflow using GitHub Actions

## Requirements

- Python 3.11 or later
- Git
- GitHub account

## Run the tests locally

```powershell
python -m unittest -v test_library.py
```

## Continuous Integration

The GitHub Actions workflow is located at:

.github/workflows/library-ci.yml

The workflow runs the automated tests on pushes and pull
requests targeting the main branch.

## Expected result

The test suite contains 12 tests. Check the terminal output
and GitHub Actions run to confirm the actual result.
