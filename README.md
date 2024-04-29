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
* Output after running the pylint.yml file
  
![WORKFLOW](https://github.com/justin494/ADA_LAB_FAT_PYTHON_WEBSITE/assets/78421431/1f6bb9d9-179f-4556-9a63-969a7fcb5f50)

# CI/CD pipeline steps

```
 Step 1 - Signup and Login to GitHub.com
 Step 2 - Create a new Repository
 Step 3 - In the repo create a folder .github/workflows
 Step 4 - In the folder create a YAML file with .yml extension
 Step 5 - Add the content of the workflow in the file
 Step 6 - Commit and push the changes
 Step 7 - Goto Repo main page and click “Actions” tab
 Step 8 - Select the workflow from left sidebar and check the logs and results

 Terms:
 WORKFLOW : collection of jobs, defined in a YAML file
 name:
 EVENTS : any activity in the repo that can trigger a workflow 
 on:
 JOBS : collection of steps
 jobs:
 STEPS : actions to be taken, commands, scripts
 steps:
 Chain Jobs - :needs

```
![ada3](https://github.com/justin494/ADA_LAB_FAT_PYTHON_WEBSITE/assets/78421431/2d5cccc4-b1bb-4315-a327-67fc649f5021)


![ada4](https://github.com/justin494/ADA_LAB_FAT_PYTHON_WEBSITE/assets/78421431/f8c30235-c8eb-47c5-b43e-e9bc7693ce66)


