"""Figure 4A schematic: atlas construction via a Set Transformer classifier.

Cells -> Cell-DINO embeddings -> Set Transformer classifier -> prediction
performance. Cells are ranked by their per-cell contribution to the classifier's
predictive accuracy (bar length); the top-k form the "Top-predictive cells".
The classifier predicts either a gene KO / NTC label (n=1,001) or a protein
complex (n=99).

Outputs editable SVG (+ PNG) with embedded fonts (pdf.fonttype 42).
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, FancyBboxPatch, Ellipse
import numpy as np

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica", "DejaVu Sans"]

# ---- palette (pink -> purple) --------------------------------------------
CELL_COLORS = ["#d94f9a", "#b8368a", "#6f3f97", "#e78fc0", "#5e3a87", "#d94f9a"]
INK = "#1a1a1a"
GREY = "#7a7a7a"


def _arrow(ax, x0, y0, x1, y1, lw=1.6, color=INK, mut=12):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=mut, lw=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=5))


def build(outstem="atlas_construction_accuracy"):
    fig, ax = plt.subplots(figsize=(11.3, 6.6))
    ax.set_xlim(0, 11.3)
    ax.set_ylim(0, 6.6)
    ax.axis("off")

    # panel label
    ax.text(0.12, 6.5, "A", fontsize=36, fontweight="bold", va="top")

    r = 0.2
    row_cy = np.linspace(5.3, 3.05, 6)          # 6 cells, top->bottom

    # ---- top header row: Cells -> Cell-DINO embeddings -> Classifier -> Prediction performance ----
    hdr_y = 6.2
    ax.text(0.85, hdr_y, "Cells", fontsize=20, ha="center", va="center")
    ax.text(2.95, hdr_y + 0.17, "Cell-DINO", fontsize=20, ha="center", va="center")
    ax.text(2.95, hdr_y - 0.17, "embeddings", fontsize=20, ha="center", va="center")
    ax.text(5.45, hdr_y, "Classifier", fontsize=20, ha="center", va="center")
    ax.text(7.75, hdr_y + 0.17, "Prediction", fontsize=20, ha="center", va="center")
    ax.text(7.75, hdr_y - 0.17, "performance", fontsize=20, ha="center", va="center")
    _arrow(ax, 1.3, hdr_y, 2.0, hdr_y, mut=15)
    _arrow(ax, 3.95, hdr_y, 4.75, hdr_y, mut=15)
    _arrow(ax, 6.15, hdr_y, 6.9, hdr_y, mut=15)

    # ---- cells -----------------------------------------------------------
    cx = 0.85
    for cy, c in zip(row_cy, CELL_COLORS):
        ax.add_patch(Circle((cx, cy), r, facecolor=c, edgecolor=INK, lw=1.3, zorder=4))

    # ---- embeddings grid -------------------------------------------------
    gx0, gx1 = 1.85, 4.05
    ncol = 8
    xs = np.linspace(gx0, gx1, ncol + 1)
    for cy in row_cy:
        y0, y1 = cy - r, cy + r
        ax.add_patch(Rectangle((gx0, y0), gx1 - gx0, y1 - y0,
                               facecolor="white", edgecolor=INK, lw=1.2, zorder=3))
        for xv in xs[1:-1]:
            ax.plot([xv, xv], [y0, y1], color=INK, lw=0.8, zorder=3)

    # ---- Set Transformer box --------------------------------------------
    bx0, bx1, by0, by1 = 4.85, 6.05, 2.9, 5.45
    ax.add_patch(FancyBboxPatch((bx0, by0), bx1 - bx0, by1 - by0,
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor="white", edgecolor=INK, lw=1.6, zorder=4))
    ax.text((bx0 + bx1) / 2, (by0 + by1) / 2, "Set\nTransformer",
            fontsize=21, ha="center", va="center", rotation=90, zorder=5)

    # ---- prediction-performance ranked list (bars ~ per-cell accuracy) ---
    acc = np.array([0.42, 0.55, 0.93, 0.31, 0.88, 0.48])
    order = np.argsort(-acc)                    # descending
    k = 2                                       # top-k = top-predictive cells
    lx = 6.9
    rank_cy = row_cy
    for rank, idx in enumerate(order):
        cy = rank_cy[rank]
        col = CELL_COLORS[idx]
        ax.text(lx - 0.04, cy, f"{rank + 1}", fontsize=16, ha="right",
                va="center", color=INK, fontweight="bold")
        ax.add_patch(Circle((lx + 0.3, cy), 0.15, facecolor=col, edgecolor=INK,
                            lw=1.1, zorder=4))
        # performance bar: length proportional to the cell's predictive accuracy
        bar_x0, bar_w, bar_h = lx + 0.6, 1.15, 0.18
        ax.add_patch(Rectangle((bar_x0, cy - bar_h / 2), bar_w, bar_h,
                               facecolor="white", edgecolor=GREY, lw=0.9, zorder=3))
        ax.add_patch(Rectangle((bar_x0, cy - bar_h / 2), acc[idx] * bar_w, bar_h,
                               facecolor=col, edgecolor="none", zorder=4))

    # ---- bracket around the top-k -> "Top-predictive cells" --------------
    bx = lx + 1.95
    ytop, ybot = rank_cy[0] + 0.28, rank_cy[k - 1] - 0.28
    cap = 0.12
    ax.plot([bx, bx], [ybot, ytop], color=INK, lw=1.8, zorder=4)
    ax.plot([bx - cap, bx], [ytop, ytop], color=INK, lw=1.8, zorder=4)
    ax.plot([bx - cap, bx], [ybot, ybot], color=INK, lw=1.8, zorder=4)
    ax.text(bx + 0.18, (ytop + ybot) / 2, "Top-\npredictive\ncells",
            fontsize=19, ha="left", va="center")

    # ---- classifier output: predict label -> gene KO / NTC  OR  protein complex ----
    ax.text(5.45, 2.5, "predict label", fontsize=20, ha="center", va="center")
    _arrow(ax, 5.45, by0, 5.45, 2.72, mut=15)
    _arrow(ax, 5.3, 2.28, 3.75, 1.68, mut=15)
    _arrow(ax, 5.6, 2.28, 7.55, 1.68, mut=15)
    ax.text(3.55, 1.5, "gene KO / NTC\n($n$ = 1,001 choices)", fontsize=19, ha="center", va="top")
    ax.text(5.55, 1.42, "OR", fontsize=19, ha="center", va="top", fontweight="bold")
    ax.text(7.85, 1.5, "protein complex\n($n$ = 99 choices)", fontsize=19, ha="center", va="top")

    # ---- input: bag of N cells (bottom-left, tidy flower packing) --------
    bag_cx, bag_cy = 1.15, 1.55
    ax.add_patch(Ellipse((bag_cx, bag_cy), 1.55, 1.05, facecolor="white",
                         edgecolor=INK, lw=1.5, zorder=3))
    pts = [(0.0, 0.0)]                                   # centre + 5-ring
    for a in np.deg2rad(np.linspace(90, 90 + 288, 5)):
        pts.append((0.46 * np.cos(a), 0.31 * np.sin(a)))
    for (px, py), col in zip(pts, CELL_COLORS):
        ax.add_patch(Circle((bag_cx + px, bag_cy + py), 0.135,
                            facecolor=col, edgecolor=INK, lw=0.9, zorder=4))
    ax.text(bag_cx, 0.78, "bag of\n$N$ cells", fontsize=19, ha="center", va="top")

    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.01)
    for ext in ("svg", "png"):
        fig.savefig(f"{outstem}.{ext}", dpi=300, bbox_inches="tight",
                    facecolor="white")
    print(f"wrote {outstem}.svg and {outstem}.png")
    return fig


if __name__ == "__main__":
    build()
