# CZ Biohub publication repository template 

This repo contains a template for starting new publication repository at the Biohub. It is prepared 
to help to organize publication related materials.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# One-time: install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies (creates .venv/, reads uv.lock)
uv sync

# Launch JupyterLab
uv run jupyter lab
```

## Usage

Notebooks under `notebooks/figure_*/` can be run interactively in JupyterLab,
or executed end-to-end from the command line with the helper script:

```bash
# Re-run every notebook in the repo
scripts/run_notebooks.sh

# Re-run only the notebooks for a single figure
scripts/run_notebooks.sh figure_5
```

## Development

One-time setup after cloning:

```bash
# Enable the pre-commit hook that strips notebook outputs before commit
uv run pre-commit install

# Link the data/ directory to the central HPC analysis folder
# (Biohub HPC only; on public release, replace this with the figshare download)
ln -s /hpc/projects/icd.fast.ops/paper_v1_analysis data
```
Needs to be changed
The notebooks read h5ad files from `/hpc/projects/icd.fast.ops/...`; you must have read access to that path (Biohub HPC).

## Organization
The structure of this repo is illustrated below.
```
├── notebooks/
│   ├── figure_1/
│   │   ├── experiment_correlations.ipynb
│   │   └── README.md
│   ├── figure_2/
│   │   ├── model_comparison.ipynb
│   │   └── README.md
│   └── figure_5/
│       ├── rna_ops_metrics.ipynb
│       └── README.md
├── scripts/
├── output/              # generated figures (figure_1/, figure_2/, figure_5/)
├── pyproject.toml
├── uv.lock
├── .python-version
├── LICENSE
└── README.md
```

