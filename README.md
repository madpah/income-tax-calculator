# Income Tax Calculator

[![Build Status](https://travis-ci.org/madpah/income-tax-calculator.svg?branch=master)](https://travis-ci.org/madpah/income-tax-calculator)

This is a sample project and is not intended to be able to calculate tax according to UK or any other territories Income 
Tax Rules. **Please do not use this to inform on anyone's actual tax position!**

## Installation

### Requirements

Python 3+ is required to bootstrap this project. It was developed against version 3.7.3.

### Local Setup

1. Clone this git repository (e.g. into /my/code/income-tax-calculator)
2. Create your virtual environment: (note: PyCharm may assist you automatically with this):
> This can be achieved through the IDE or by running the command below
 ```
 # Ensure you are in the project folder
 cd /my/code/income-tax-calculator
 
 # Create a new Python 3 Virtual Environment in folder named 'venv'
 python3 -m venv venv
 ```
3. Install the required python module dependencies:
 ```
 # Ensure you are in the project folder
 cd /my/code/income-tax-calculator
 
 # Ensure the Python Virtual Environment is active
 . venv/bin/activate
 
 # Install our requirements (requires Internet connectivity)
 pip install -f requirements.txt
 ```
3. Open the project in PyCharm and ensure PyCharm has detected / understood you have a virtual environment in the folder
 named *venv*.

### Development Setup

Follow the steps above, but additionally, you may wish to install the git hooks which help ensure quality. To
do so, copy the contents of _.git_hooks_ directory to your local git repositories hooks directory:

```
cp /my/code/income-tax-calculator/.git-hooks/* /my/code/income-tax-calculator/.git/hooks
```

#### Linting

This project utilises [Flake8](https://gitlab.com/pycqa/flake8) to lint our source according to 
[PEP8](https://www.python.org/dev/peps/pep-0008/) standards.

Linting can be performed manually by running the following from inside your Python Virtual Environment:
```
flake8
```

If you have installed the supplied git hooks - linting is performed pre-commit.

#### Testing

Unit and Integration Tests are written using the 
[Python unittest framework](https://docs.python.org/3/library/unittest.html).

They can be run from inside PyCharm or by running the following command from inside your Python Virtual Environment:
```
python -m unittest discover -s tests/
```

If you have installed the supplied git hooks - tests are executed pre-commit.

## Running

The project can be run in one of two ways:

1. Directly invoking Python
2. Via the helper script

Coming soon...