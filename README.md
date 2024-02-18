# Benders Calliope
## About
Applying Benders' decomposition to [Calliope models](https://github.com/calliope-project/calliope). This Repo is a work-in-progress and meant for experimentation with Benders' decomposition.

## Setup
This project uses Calliope as a dependency. The other major dependency is a (MI)LP solver.
Following the suggestion in the [Calliope docs](https://calliope.readthedocs.io/en/stable/user/installation.html), we use the conda package manager to install calliope. To install conda see the [Conda docs](https://docs.anaconda.com/free/miniconda/). Then

```bash
conda update -n base -c conda-forge conda
conda create -c conda-forge -n benders_calliope calliope
conda install -c conda-forge -n benders_calliope --file requirements.txt
conda activate benders_calliope
```
