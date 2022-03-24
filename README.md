# cookiecutter-python-project
A template for python projects made using cookiecutter.
## Structure

    .
    ├── LICENSE
    ├── environment.yml
    ├── .gitignore
    ├── README.md
    ├── setup.py
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── figures
    ├── notebooks
    ├── references
    ├── reports
    ├── src
        ├── init.py
        ├── analysis
        ├── etl
        ├── utils
        └── viz

- `LICENSE`
  - License file for the project.
  - Availiable options include MIT and BSD-3-Clause.
- `environment.yml`
  - The requirements file to reproduce the analysis environment. 
- `.gitignore`
  - Ignores python user profile temporary files.
- `README.md`
  - Project specific readme.
- `setup.py`
  - Makes project pip installable with `pip install -e ../`.
- `data`
  - This is the directory used to store all of the project's data. All files should go into one of the following folders.
  - `data/external`
    - Data from third party sources.
  - `data/interim`
    - Intermediate data that has been transformed.
  - `data/processed`
    - The final, canonical data sets for analysis.
  - `data/raw`
    - The original, inmutable data dump.
- `figures`
  - Generated graphics and figures to be used in reporting.
- `notebooks`
  - Any Jupyter Notebooks go here.
- `references`
  - Data dictionaries, manuals, and all other exploratory materials.
- `reports`
  - Generated analysis as HTML, PDF, LaTeX, etc.
- `src`
  - All the scripts in the project go here.
  - `src/__init__.py`
    - Makes `src` a Python module.
  - `src/analysis`
    - Code that involves analysis on already-cleaned data. Code for cleaning data should go in `src/etl`.
    - Multiple analysis files are numbered sequentially.
  - `src/etl`
  - ETL (extract, transform, load) scripts for reading in source data, cleaning and standardizing it to prepare for analysis go here.
    - Joins are included in ETL process.
    - Multiple ETL files are numbered sequentially.
  - `src/utils`
    - Miscellaneous code goes here.
  - `src/viz`
    - Graphics and visualization development specific work should go here.
    - Multiple viz files are numbered sequentially.
  

## Requirements

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [Cookiecutter Python package](https://cookiecutter.readthedocs.io/en/latest/installation.html)

This can be installed using either

```shell
pip install cookiecutter
```

or

```shell
conda install -c conda-forge cookiecutter
```

## Installation

In the folder where you want to generate the project, run:

```shell
cookiecutter https://github.com/camartinezbu/cookiecutter-python-project
```

If you wish to create a conda environment based on the `environment.yml` file, run:

```shell
# Go to the project's directory:
cd DIRECTORY_NAME

# Create a conda environmenT:
conda env create --file environment.yml

# Activate said environment:
conda activate ENVIRONMENT_NAME
```

> Both `DIRECTORY_NAME` and `ENVIRONMENT_NAME` correspond to the project's slug name, defined when creating the template.

### Set up prohect's module

In order to set up the project's module, in the terminal run:

```shell
pip install -e ../
```

Or if you are in a notebook, run in a code cell:

```shell
! pip install -e --/
```

To use the module inside the notebook, add the following to the first cell:

```shell
%load_ext autoreload
%autoreload 2
```

## Credits

This template was designed based on [jvelesmagic's Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-science).

## Extra

Check out a similar template for R [here](https://github.com/camartinezbu/cookiecutter-r-project).
