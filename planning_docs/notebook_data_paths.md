# Notebook Data Paths

Data paths used by each notebook in the repo, extracted from the notebook source.

## Figure 1

### `notebooks/figure_1/experiment_correlations.ipynb`

- Precomputed experiment-experiment cosine similarity matrix (produced by `data_preprocessing/figure_1.py`):
  `/hpc/mydata/alexander.hillsley/ops/ops-paper-analysis/data_preprocessing/data/experiment_correlations_sim_matrix.csv`

### `notebooks/figure_1/iss_correlation_heatmap.ipynb`

- Precomputed experiment × experiment Pearson correlation matrix on log2 mean-normalised ISS barcode read frequencies (produced by `ops_monorepo/ops_model/analysis/iss_correlation_heatmap.py`):
  `data/figures/figure_1/iss_barcode_freq_correlation_matrix.csv`

## Figure 2

### `notebooks/figure_2/model_comparison.ipynb`

Base directory: `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3`

Per model, three evaluation CSVs under `{model}/zscore_per_exp/paper_v1/all_livecell/fixed_80%/cosine/second_pca_consensus/metrics/`:

**cell_dino**
- `cell_dino/.../metrics/phenotypic_activity.csv`
- `cell_dino/.../metrics/phenotypic_distinctiveness.csv`
- `cell_dino/.../metrics/phenotypic_consistency_manual.csv`

**dino**
- `dino/.../metrics/phenotypic_activity.csv`
- `dino/.../metrics/phenotypic_distinctiveness.csv`
- `dino/.../metrics/phenotypic_consistency_ebi.csv`

**cellprofiler**
- `cellprofiler/.../metrics/phenotypic_activity.csv`
- `cellprofiler/.../metrics/phenotypic_distinctiveness.csv`
- `cellprofiler/.../metrics/phenotypic_consistency_ebi.csv`

**dynaclr**
- `dynaclr/.../metrics/phenotypic_activity.csv`
- `dynaclr/.../metrics/phenotypic_distinctiveness.csv`
- `dynaclr/.../metrics/phenotypic_consistency_ebi.csv`

**subcell**
- `subcell/.../metrics/phenotypic_activity.csv`
- `subcell/.../metrics/phenotypic_distinctiveness.csv`
- `subcell/.../metrics/phenotypic_consistency_ebi.csv`

## Figure 3

### `notebooks/figure_3/reporter_titration_plots.ipynb`

- Merged per-reporter titration CSV (full log range + 50–1000 cells/guide zoom; produced by `data_preprocessing/figure_3.py`):
  `/hpc/mydata/alexander.hillsley/ops/ops-paper-analysis/data_preprocessing/data/titration_individual_reporters.csv`

### `notebooks/figure_3/combined_reporter_titration.ipynb`

- Combined-reporter aggregates (cp / 4i / live-cell-matched / full live-cell):
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/with_cp/with_4i/all_livecell/fixed_80%/cosine/combined_titration_compare/per_guide_median/cp_vs_4i_vs_matched_livecell_best_vs_livecell/compare_all_metrics_cells_per_guide.csv`

### `notebooks/figure_3/reporter_mAP_histogram.ipynb`

- Per-gene distinctiveness per reporter (with an extra `all_combined` column for the all-reporters-combined embedding):
  `/hpc/mydata/alexander.hillsley/ops/ops_monorepo/ops_model/analysis/heatmaps/gene_reporter_distinctiveness_raw.csv`

### `notebooks/figure_3/reporters_vs_essentiallity.ipynb`

- Per-gene distinctiveness per reporter (genes × reporters, with `all_combined` column dropped before counting markers):
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/all_livecell/fixed_80%/cosine/second_pca_consensus/plots/marker_overlay/gene_reporter_distinctiveness_raw.csv`
- CERES gene-effect table (twist1k pool):
  `/hpc/projects/icd.fast.ops/configs/library/twist1k_pool_CERES.csv`

### `notebooks/figure_3/marker_similarity_clustermap.ipynb`

- Per-gene × per-reporter distinctiveness matrix (genes × reporters; `all_combined` column dropped, four 4i markers excluded at load):
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/with_cp/with_4i/all_livecell/fixed_80%/cosine/second_pca_consensus/plots/marker_overlay/gene_reporter_distinctiveness_raw.csv`
- Per-marker organelle metadata (short name, category, color, category rank; produced by `data_preprocessing/marker_organelle_metadata.py`):
  `/hpc/mydata/alexander.hillsley/ops/ops-paper-analysis/data_preprocessing/data/marker_organelle_metadata.csv`

## Figure 5

### `notebooks/figure_5/joint_heatmap.ipynb`

- OPS gene-level embeddings (cell_dino, Phase-only):
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/phase_only/fixed_80%/cosine/gene_pca_optimized.h5ad`
- CROP-Seq sVAEplus perturbation-level embeddings (W matrix in `.uns`):
  `/hpc/projects/data.science/duo.peng/sVAEplus/sVAEplus/6000HVG/svaeplus_results_2_256_1_200_0.5/svaeplus_embeddings.h5ad`

### `notebooks/figure_5/rna_ops_metrics.ipynb`

- Crop-seq sVAEplus distinctiveness (std_ntc variant):
  `/hpc/projects/data.science/duo.peng/sVAEplus/sVAEplus/6000HVG/svaeplus_results_2_256_1_200_0.5/mAP_distinctiveness_std_ntc.csv`
- OPS cell_dino All-Fluorescence (no_phase) distinctiveness:
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/no_phase/fixed_80%/cosine/second_pca_consensus/metrics/phenotypic_distinctiveness.csv`
- OPS cell_dino All-Fluorescence (no_phase) EBI:
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/no_phase/fixed_80%/cosine/second_pca_consensus/metrics/phenotypic_consistency_ebi.csv`
- OPS cell_dino Phase-only distinctiveness:
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/phase_only/fixed_80%/cosine/metrics/phenotypic_distinctiveness.csv`
- OPS cell_dino Phase titration:
  `/hpc/projects/icd.fast.ops/organelle_attribution/pca_optimized_v0.3/cell_dino/zscore_per_exp/paper_v1/with_cp/with_4i/all_livecell/fixed_80%/cosine/titration_guide_median/Phase/Phase_titration.csv`
- Crop-seq EBI mAP (currently in ops_monorepo scratch; move before release):
  `/hpc/mydata/alexander.hillsley/ops/ops_monorepo/experiments/scratch/crop-seq/20260520_mAP_ebi_cropseq.csv`
