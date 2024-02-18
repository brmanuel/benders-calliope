# Benders Calliope
## About
Applying Benders' decomposition to [Calliope models](https://github.com/calliope-project/calliope).

## Setup
This project uses Calliope as a dependency. The other major dependency is a (MI)LP solver.
Following the suggestion in the [Calliope docs](https://calliope.readthedocs.io/en/stable/user/installation.html), we use the conda package manager to install calliope. To install conda see the [Conda docs](https://docs.anaconda.com/free/miniconda/). Then

```bash
conda create -c conda-forge -n benders_calliope calliope
conda activate benders_calliope
conda install -c conda-forge pyscipopt
```
