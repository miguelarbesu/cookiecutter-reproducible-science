Reproducible Science
====================

This is a template for Python-based data analysis workflows and tools. It's a fork from Mario Krapp's boilerplate for Python data science projects,
[Reproducible Science](https://github.com/miguelarbesu/cookiecutter-reproducible-science). The original derives from [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science): *A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.*

Here I reintroduce some elements according to my own needs and preferences.

Other important sources of inspiration are:

- Scott Torborg's [Minimal structure](https://python-packaging.readthedocs.io/en/latest/minimal.html)
- João M.C. Teixeira's [Python project skeleton](https://github.com/joaomcteixeira/python-project-skeleton)
- MolSSI's [Cookiecutter for Computational Molecular Sciences (CMS) Python Packages](https://github.com/MolSSI/cookiecutter-cms)

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`    

Usage
-----
To start a new science project from this version of the template:

`cookiecutter gh:miguelarbesu/cookiecutter-reproducible-science`

Project Structure
-----------------

```
.
├── AUTHORS.md
├── LICENSE
├── README.md
├── setup.py           <- Installation script
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── notebooks          <- Jupyter notebooks
├── output             <- Figures, manuscripts, or any project reports.
│   └── figures        <- Figures for the manuscript or reports
└── src                <- Source code for this project
    ├── data           <- scripts and programs to process data
    ├── external       <- Any external source code, e.g., pull other git projects, or external libraries
    ├── models         <- Source code for your own model
    ├── tools          <- Any helper scripts go here
    └── visualization  <- Scripts for visualization of your results, e.g., matplotlib, ggplot2 related.
```

License
-------
This project is licensed under the terms of the [BSD License](/LICENSE)
