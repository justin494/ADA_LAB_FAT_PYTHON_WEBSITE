# ADA_LAB_FAT_PYTHON_WEBSITE
A Flask(Python) portfolio app deployed using actions/stylelint
LAB FAT EXAM GITHUB WORKFLOWS &amp; CI/CD PIPELINE
Link of the website: https://justin494.github.io/ADA_LAB_FAT_PYTHON_WEBSITE/

# YAML File workflow code:
```
name: Pylint

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10"]
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
    - name: Analysing the code with pylint
      run: |
        pylint $(git ls-files '*.py')
```
