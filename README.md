This repository contains scripts to reproduce key figures in the paper: A multimodal perturbation atlas defines the phenotypic resolution of cellular morphology



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

Notebooks under `notebooks/` can be run interactively in JupyterLab,
or executed end-to-end from the command line with the helper script:

```bash
# Re-run every notebook in the repo
scripts/run_notebooks.sh

# Re-run only one group (a figure, or target_gene_selection)
scripts/run_notebooks.sh figure_5
scripts/run_notebooks.sh target_gene_selection
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
The notebooks read their input files from `/hpc/projects/icd.fast.ops/...`; you must have read access to that path (Biohub HPC).

## Organization
The structure of this repo is illustrated below.
```
├── notebooks/
│   ├── figure_1/
│   │   ├── experiment_correlations.ipynb
│   │   └── iss_correlation_heatmap.ipynb
│   ├── figure_2/
│   │   └── model_comparison.ipynb
│   ├── figure_3/
│   │   ├── combined_reporter_titration.ipynb
│   │   ├── marker_similarity_clustermap.ipynb
│   │   ├── reporter_mAP_histogram.ipynb
│   │   ├── reporters_vs_essentiallity.ipynb
│   │   └── reporter_titration_plots.ipynb
│   ├── figure_5/
│   │   ├── joint_heatmap.ipynb
│   │   ├── mAP_complex_KO_scatter.ipynb
│   │   ├── rna_image_confusion_matrix.ipynb
│   │   └── rna_ops_metrics.ipynb
│   └── target_gene_selection/   # gene-panel selection (no figure output)
│       └── gene_panel_selection.ipynb
├── scripts/
│   ├── analysis.sh
│   └── run_notebooks.sh
├── planning_docs/       # notebook/script & input-data-path mapping docs
├── data/                # symlink to central HPC analysis folder (gitignored)
├── output/              # generated outputs (figures + tables), one subdir per notebook group (gitignored)
├── pyproject.toml
├── uv.lock
├── .python-version
├── LICENSE
└── README.md
```

