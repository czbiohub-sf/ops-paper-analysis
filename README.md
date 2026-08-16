# A multimodal perturbation atlas defines the phenotypic resolution of cellular morphology
This repository contains scripts to reproduce key figures in the paper: [A multimodal perturbation atlas defines the phenotypic resolution of cellular morphology](https://doi.org/10.64898/2026.06.01.728087)



## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# One-time: install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository and move to it
git clone https://github.com/czbiohub-sf/ops-paper-analysis.git
cd ops-paper-analysis

# Install dependencies (creates .venv/, reads uv.lock)
uv sync

# Download the dataset (~57 MB) and extract it into data/
# (archived on Zenodo: https://doi.org/10.5281/zenodo.20495192)
mkdir -p data
curl -L -o altair_v2.zip "https://zenodo.org/records/21970895/files/altair_v2.zip?download=1"
unzip -q altair_v2.zip -d data && rm altair_v2.zip

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

## Organization
The structure of this repo is illustrated below.
```
├── notebooks/
│   ├── figure_1/
│   │   ├── experiment_correlations.ipynb
│   │   └── iss_correlation_heatmap.ipynb
│   ├── figure_2/
│   │   └── model_comparison.ipynb
│   ├── figure_3/                   # one folder per panel
│   │   ├── panel_A_schematic/
│   │   │   └── atlas_construction_schematic.py
│   │   ├── panel_B_accuracy/
│   │   │   └── eval_accuracy_curves.ipynb
│   │   ├── panel_C_scaling/
│   │   │   └── training_data_scaling.ipynb
│   │   ├── panel_D_embedding_map/
│   │   │   └── embedding_map_violin.ipynb
│   │   └── panel_L-N_traversals/
│   │       └── counterfactual_traversal_violins.ipynb
│   ├── figure_4/
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
├── data/                # folder where input data is downloaded (gitignored)
├── output/              # generated outputs (figures + tables), one subdir per notebook group (gitignored)
├── pyproject.toml
├── uv.lock
├── .python-version
├── LICENSE
├── DEVELOPMENT.md
└── README.md
```

## Authors

This repository is created and maintained by the [Leonetti Group](https://biohub.org/leonetti/) at the [Biohub in San Francisco](https://www.czbiohub.org/sf/).

To get in touch please use the [GihHub issues](https://github.com/czbiohub-sf/grassp/issues) page.
