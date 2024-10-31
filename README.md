# example_python_package

[![Unit Tests](https://github.com/jonswain/example_python_package/actions/workflows/run_tests.yml/badge.svg)](https://github.com/jonswain/example_python_package/actions/workflows/run_tests.yml)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jonswain/6b0c50d8a21d70ec5157b625d2e9a6e0/raw/example_python_package_coverage.json)

An example of creating a Python package.

## Usage and local development

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

### Create Development Environment

The following commands will setup an environment where you can develop the application locally:

```bash
git clone git@github.com/jonswain/example_python_package.git
cd example_python_package
conda env create -f envs/dev.yml
conda activate example_python_package_dev
pip install -e .
code .
```

### Production Usage

The following commands will setup an environment where you can use the application locally:

```bash
git clone git@github.com/jonswain/example_python_package.git
cd example_python_package
conda env create -f envs/prod.yml
conda activate example_python_package
pip install .
code .
```

### Running unit tests

The following commands will setup an environment where you can run the unit tests:

```bash
git clone git@github.com/jonswain/example_python_package.git
cd example_python_package
conda env create -f envs/test.yml
conda activate example_python_package_test
pip install -e .
code .
```

To run the unit tests and check coverage:

```bash
coverage run -m --source=src pytest -v -s
coverage report -m
```
