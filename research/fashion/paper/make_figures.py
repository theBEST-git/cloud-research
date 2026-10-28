"""Paper figures that need no outcome. Figure 1 (waves): share of discovery submissions (with text) listing an author
keyword, 2018-2026, one small panel per keyword, peak marked. Keywords: waves named in the paper (PH6 waves plus the
earlier GAN and meta-learning waves and the rising diffusion and LLM waves).

    python research/fashion/paper/make_figures.py      -> research/fashion/paper/figs/fig1_waves.{pdf,png}
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from common import CORPUS, topic_layer  # noqa: E402

assert CORPUS == "discovery", "run with ICLR_CORPUS unset: the figures show the discovery split"
FIGS = HERE / "figs"
BLUE, INK, INK2, MUTED, GRID = "#2a78d6", "#0b0b0b", "#3a3a38", "#7a7974", "#e4e3df"
YEARS = np.arange(2018, 2027)
WAVES = [("generative adversarial networks", "GANs"), ("adversarial attack", "Adversarial attacks"),
         ("meta-learning", "Meta-learning"), ("graph neural networks", "Graph neural nets"),
         ("federated learning", "Federated learning"), ("self-supervised learning", "Self-supervised"),
         ("diffusion models", "Diffusion models"), ("large language models", "Large language models")]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2, "axes.linewidth": 0.8,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True,
                     "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True, "axes.spines.top": False,
                     "axes.spines.right": False})


def shares() -> dict[str, np.ndarray]:
    c = topic_layer().embedded_corpus()
    c = c[c.year.between(YEARS[0], YEARS[-1])]
    total = c.groupby("year").size().reindex(YEARS).to_numpy(float)
    return {kw: 100 * c[c.keywords.apply(lambda s, kw=kw: kw in s)].groupby("year").size()
            .reindex(YEARS, fill_value=0).to_numpy(float) / total for kw, _ in WAVES}


def waves() -> None:
    sh = shares()
    fig, axes = plt.subplots(2, 4, figsize=(7.0, 3.0), sharex=True)
    for ax, (kw, label) in zip(axes.ravel(), WAVES):
        y = sh[kw]
        i = int(np.argmax(y))
        ax.fill_between(YEARS, y, color=BLUE, alpha=0.15, lw=0)
        ax.plot(YEARS, y, color=BLUE, lw=1.8)
        ax.plot(YEARS[i], y[i], "o", color=BLUE, ms=4)
        ha = "left" if i <= 1 else "right" if i == len(YEARS) - 1 else "center"
        ax.annotate(f"{y[i]:.1f}% ({YEARS[i]})", (YEARS[i], y[i]), xytext=(0, 4), textcoords="offset points", ha=ha,
                    va="bottom", fontsize=7, color=INK)
        ax.set_ylim(0, y.max() * 1.35)
        ax.set_title(label, fontsize=8.5, color=INK, loc="left")
        ax.set_xticks([2018, 2022, 2026], ["'18", "'22", "'26"])
        ax.tick_params(labelsize=7.5, length=2)
        ax.yaxis.set_major_locator(plt.MaxNLocator(3))
    for ax in axes[:, 0]:
        ax.set_ylabel("% of subm.", fontsize=8)
    fig.tight_layout(w_pad=0.6, h_pad=0.8)
    FIGS.mkdir(exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(FIGS / f"fig1_waves.{ext}", dpi=220, bbox_inches="tight")
    plt.close(fig)
    for kw, label in WAVES:
        y = sh[kw]
        print(f"{label}: peak {y.max():.1f}% ({YEARS[np.argmax(y)]}), 2026 {y[-1]:.1f}%")


if __name__ == "__main__":
    waves()
