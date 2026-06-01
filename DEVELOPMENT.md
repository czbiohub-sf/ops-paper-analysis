# Development

Setup for contributors (after cloning and completing the README **Setup** steps):

```bash
# Pre-commit hook: strips notebook outputs before each commit
uv run pre-commit install
```

`scripts/run_notebooks.sh` re-executes notebooks in place; the pre-commit hook
strips their outputs again before commit, so re-running before pushing is safe.

```bash
scripts/run_notebooks.sh              # re-run every notebook
scripts/run_notebooks.sh figure_5     # re-run only one group
```

## Data (Biohub HPC)

Instead of downloading the dataset (see README **Setup**), Biohub HPC users can
symlink the central analysis folder directly:

```bash
ln -s /hpc/projects/icd.fast.ops/paper_v1_analysis data
```
