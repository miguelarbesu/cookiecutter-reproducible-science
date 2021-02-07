# Reproducible Science

This is a template for Python-based data analysis workflows and tools. It's a fork from Mario Krapp's boilerplate for Python data science projects,
[Reproducible Science](https://github.com/miguelarbesu/cookiecutter-reproducible-science). The original derives from [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science): *A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.*

Here I reintroduce some elements according to my own needs and preferences.Other important sources of inspiration are:

- Scott Torborg's [Minimal structure](https://python-packaging.readthedocs.io/en/latest/minimal.html)
- João M.C. Teixeira's [Python project skeleton](https://github.com/joaomcteixeira/python-project-skeleton)
- MolSSI's [Cookiecutter for Computational Molecular Sciences (CMS) Python Packages](https://github.com/MolSSI/cookiecutter-cms)
- Allen Institute for Cell Science's [Cookeicutter pypackage](https://github.com/AllenCellModeling/cookiecutter-pypackage)

## Requirements

Install `cookiecutter` from [Pip](https://pypi.org/project/pip/) or [Conda](https://docs.conda.io/en/latest/).

## Usage

To start a new science project from this version of the template:

`cookiecutter gh:miguelarbesu/cookiecutter-reproducible-science --checkout main`

If you have a local install, you can run:

`cookiecutter ./cookiecutter-reproducible-science --checkout main`

## Structure

```
├─ data                             <--- Experimental data
│  ├─ external                          
│  ├─ interim
│  ├─ processed
│  └─ raw
├─ devtools                         <--- Development tools
├─ doc                              <--- Project documentation
├─ notebook                         <--- Exploratory Jupyter notebooks
├─ output                           <--- Final analysis report
│  └─ figures
├─ src
│  ├─ packagename
│  │  ├─ __init__.py
│  │  ├─ __main__.py
│  │  └─ modulename.py
│  ├─ data
│  └─ tests
│     ├─ __init__.py
|     └─ test_modulename.py
└─ setup.py
```

## Features

- Unit testing with [Pytest](https://docs.pytest.org/en/stable/).
- Packaging with [Pip Setuptools](https://setuptools.readthedocs.io/en/latest/)
<!-- 
- Environment management with conda/pyenv/virtualenv ...
- Linting with black.
- CI with Github Actions.
- Documentation with Mkdocs/Sphinx/...
- Makefile
 -->

## Workflow

Typically, I will start analyzing a given data set(s) with experimental results
and/or a reference database from others. My own data will be saved as an
immutable dump under `raw`, third-party under `external`. Then usually follows an exploratory stage to evaluate & clean the data. Intermediate data belong to `interim`. Finally, some kind of elaborated data is derived -- e.g. parameters from a fitting -- the `processed` data.

I use to start exploring data in Jupyter notebooks under `/notebooks`, writing
basic functions to delineate a piece of the analysis pipeline, then refactor it
under `/src` once it is functional. This exploratory phase should not eclipse
proper coding: write directly in the module and start writing tests soon.

At this point, the nature of the project should define the form of the
repository. For a **one-off analysis** of a small set of measurement, a simple
module usually does the trick and one will not bother distributing a proper package. This does not mean lousy code: document and test properly, as this
small pieces can be needed in the future, or incorporated in larger projects. An example of this is the code associated to figures in a research article.

For **recurrent analysis** on new data sets of the same kind, a proper tool is needed. Usually, a Command Line Interface (CLI) is [the way to go](https://github.com/joaomcteixeira/python-project-skeleton/blob/master/src/sampleproject/cli_int1.py). Turning a module into a CLI is natural in Python, it just involves a parsing layer module. While [Argparse](https://docs.python.org/3/library/argparse.html) is the basic tool, [Click](https://click.palletsprojects.com/en/7.x/) is easy and powerful. Further down the road one may want to create a GUI.

For **large scale pipeline analysis** with a [ DAG structure](https://drivendata.github.io/cookiecutter-data-science/) -- e.g. bioinformatics studies, processing thousands of files -- a Makefile is desirable. Software Carpentry has a [great tutorial](https://swcarpentry.github.io/make-novice/) on the topic. 

The distilled information derived from the analysis is usually presented in the form of plots, integrated in a report. A jupyter notebook is usually a good format to put all this together in an interactive and exportable format.
All this material is finally found under `output` and `output/figures`.

## License

This project is licensed under the terms of the [BSD License](/LICENSE)
