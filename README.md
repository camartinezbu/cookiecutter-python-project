# cookiecutter-python-project
A template for python projects made using cookiecutter.
## Structure

    .
    ├── LICENSE
    ├── environment.yml
    ├── .Rprofile
    ├── .gitignore
    ├── README.md
    ├── analysis
    │   └── notebooks
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── etl
    ├── reports
    ├── references
    ├── viz
        └── figures

- `LICENSE`
  - License file for the project.
  - Availiable options include MIT and BSD-3-Clause.
- `environment.yml`
  - The requirements file to reproduce the analysis environment. 
- `.gitignore`
  - Ignores python user profile temporary files.
- `README.md`
  - Project specific readme.
- `analysis`
  - R code that involves analysis on already-cleaned data. Code for cleaning data should go in `etl`.
  - Multiple analysis files are numbered sequentially.
    - `analysis/notebooks`
      - Any R Markdown files go here.
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
- `etl`
  - ETL (extract, transform, load) scripts for reading in source data, cleaning and standardizing it to prepare for analysis go here.
    - Multiple ETL files are numbered sequentially.
    - Joins are included in ETL process.
- `reports`
  - Generated analysis as HTML, PDF, LaTeX, etc.
- `references`
  - Data dictionaries, manuals, and all other exploratory materials.
- `viz`
  - Graphics and visualization development specific work should go here.
    - Multiple viz files are numbered sequentially.
  - `viz/figures`
    - Generated graphics and figures to be used in reporting.


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

## Credits

This template was designed based on [jvelesmagic's Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-science).

## Extra

Check out a similar template for R [here](https://github.com/camartinezbu/cookiecutter-r-project).