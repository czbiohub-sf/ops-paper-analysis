"""Figure 4A schematic: atlas construction via a Set Transformer classifier.

This version highlights cell selection by *predictive accuracy* (per-cell
contribution to the classifier's accuracy) rather than by attention weight.
Cells are ranked and the top-k are checkmarked -> "Top Accuracy Cells".

Outputs editable SVG (+ PNG) with embedded fonts (pdf.fonttype 42).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, FancyBboxPatch, Ellipse
from matplotlib.collections import LineCollection
import numpy as np

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica", "DejaVu Sans"]

# ---- palette (pink -> purple, matching original) -------------------------
CELL_COLORS = ["#d94f9a", "#b8368a", "#6f3f97", "#e78fc0", "#5e3a87", "#d94f9a"]
INK = "#1a1a1a"
GREY = "#7a7a7a"
CHECK = "#2e7d32"
SEL_EDGE = "#2e7d32"


def _arrow(ax, x0, y0, x1, y1, lw=1.6, color=INK, mut=12):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=mut, lw=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=5))


def _check(ax, cx, cy, s=0.11, color=CHECK, lw=2.4):
    seg = [[(cx - s, cy), (cx - s * 0.25, cy - s * 0.9)],
           [(cx - s * 0.25, cy - s * 0.9), (cx + s * 1.1, cy + s)]]
    ax.add_collection(LineCollection(seg, colors=color, linewidths=lw,
                                     capstyle="round", zorder=6))


def build(outstem="atlas_construction_accuracy"):
    fig, ax = plt.subplots(figsize=(11.3, 6.6))
    ax.set_xlim(0, 11.3)
    ax.set_ylim(0, 6.6)
    ax.axis("off")

    # panel label + title
    ax.text(0.12, 6.48, "A", fontsize=36, fontweight="bold", va="top")
    ax.text(0.82, 6.46, "Atlas construction", fontsize=28, va="top")

    hdr_y = 5.85
    row_cy = np.linspace(5.35, 3.1, 6)          # 6 cells, top->bottom
    r = 0.2

    # ---- column headers --------------------------------------------------
    ax.text(0.85, hdr_y, "Cells", fontsize=20, ha="center")
    ax.text(2.95, hdr_y, "Embeddings", fontsize=20, ha="center")
    ax.text(5.45, hdr_y, "classifier", fontsize=20, ha="center")
    ax.text(7.75, hdr_y + 0.2, "Predictive", fontsize=20, ha="center")
    ax.text(7.75, hdr_y - 0.18, "Accuracy", fontsize=20, ha="center")

    # ---- header arrows ---------------------------------------------------
    _arrow(ax, 1.2, hdr_y - 0.02, 1.9, hdr_y - 0.02, mut=15)
    _arrow(ax, 4.05, hdr_y - 0.02, 4.85, hdr_y - 0.02, mut=15)
    _arrow(ax, 6.05, hdr_y - 0.02, 6.85, hdr_y - 0.02, mut=15)

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
    bx0, bx1, by0, by1 = 4.85, 6.05, 2.95, 5.5
    ax.add_patch(FancyBboxPatch((bx0, by0), bx1 - bx0, by1 - by0,
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor="white", edgecolor=INK, lw=1.6, zorder=4))
    ax.text((bx0 + bx1) / 2, (by0 + by1) / 2, "Set\nTransformer",
            fontsize=21, ha="center", va="center", rotation=90, zorder=5)

    # ---- predictive-accuracy ranked list (checkmarks, not bars) ----------
    # per-cell accuracy contribution; ranked descending. top-k selected.
    acc = np.array([0.42, 0.55, 0.93, 0.31, 0.88, 0.48])
    order = np.argsort(-acc)                    # descending
    k = 2                                       # selected top-k
    lx = 6.9                                    # left of ranked column
    rank_cy = np.linspace(5.35, 3.1, 6)
    for rank, idx in enumerate(order):
        cy = rank_cy[rank]
        selected = rank < k
        col = CELL_COLORS[idx]
        # rank chip
        ax.text(lx - 0.04, cy, f"{rank + 1}", fontsize=16, ha="right",
                va="center", color=INK if selected else GREY, fontweight="bold")
        # cell dot (faded if not selected)
        alpha = 1.0 if selected else 0.4
        ax.add_patch(Circle((lx + 0.3, cy), 0.15, facecolor=col, edgecolor=INK,
                            lw=1.1, alpha=alpha, zorder=4))
        # performance bar: length ∝ predictive accuracy (the cell's set-classification contribution)
        bar_x0, bar_w, bar_h = lx + 0.6, 1.15, 0.18
        ax.add_patch(Rectangle((bar_x0, cy - bar_h / 2), bar_w, bar_h,
                               facecolor="white", edgecolor=GREY, lw=0.9, zorder=3, alpha=alpha))
        ax.add_patch(Rectangle((bar_x0, cy - bar_h / 2), acc[idx] * bar_w, bar_h,
                               facecolor=col, edgecolor="none", zorder=4, alpha=alpha))

    # ---- bracket around the top-k ranked cells -> "Top Predictive Cells" --
    bx = lx + 1.95                               # right of the performance bars
    ytop, ybot = rank_cy[0] + 0.28, rank_cy[k - 1] - 0.28
    cap = 0.12
    ax.plot([bx, bx], [ybot, ytop], color=INK, lw=1.8, zorder=4)          # spine
    ax.plot([bx - cap, bx], [ytop, ytop], color=INK, lw=1.8, zorder=4)    # top cap (toward cells)
    ax.plot([bx - cap, bx], [ybot, ybot], color=INK, lw=1.8, zorder=4)    # bottom cap
    ax.text(bx + 0.18, (ytop + ybot) / 2, "Top\nPredictive\nCells",
            fontsize=19, ha="left", va="center", fontweight="bold")

    # ---- lower flow: bag of N cells / predict label ----------------------
    bag_cx, bag_cy = 5.45, 2.05
    _arrow(ax, (bx0 + bx1) / 2, by0, bag_cx, bag_cy + 0.42, mut=15)
    ax.add_patch(Ellipse((bag_cx, bag_cy), 1.2, 0.8, facecolor="white",
                         edgecolor=INK, lw=1.5, zorder=3))
    rng = np.random.default_rng(0)
    for _ in range(7):
        dx = rng.uniform(-0.32, 0.32)
        dy = rng.uniform(-0.18, 0.18)
        ax.add_patch(Circle((bag_cx + dx, bag_cy + dy), 0.06,
                            facecolor=INK, edgecolor="none", zorder=4))
    ax.text(bag_cx + 0.9, bag_cy + 0.05, "bag of\n$N$ cells", fontsize=19,
            ha="left", va="center")

    ax.text(bag_cx, 1.25, "predict label", fontsize=20, ha="center", va="center")
    _arrow(ax, bag_cx, bag_cy - 0.42, bag_cx, 1.45, mut=15)

    # split arrows
    _arrow(ax, bag_cx - 0.15, 1.02, 3.35, 0.55, mut=15)
    _arrow(ax, bag_cx + 0.15, 1.02, 7.55, 0.55, mut=15)
    ax.text(2.9, 0.32, "knockout + NTC\n($n$ = 1,001 choices)", fontsize=19, ha="center", va="top")
    ax.text(5.45, 0.4, "OR", fontsize=19, ha="center", va="top", fontweight="bold")
    ax.text(8.0, 0.32, "protein complex\n($n$ = 91 choices)", fontsize=19, ha="center", va="top")

    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.01)
    for ext in ("svg", "png"):
        fig.savefig(f"{outstem}.{ext}", dpi=300, bbox_inches="tight",
                    facecolor="white")
    print(f"wrote {outstem}.svg and {outstem}.png")
    return fig


if __name__ == "__main__":
    build()
