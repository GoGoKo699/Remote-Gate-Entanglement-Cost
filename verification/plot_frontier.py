#!/usr/bin/env python3
"""Plot analytic lower/upper bounds, not fitted or empirical performance."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from bounds import lower_bound, upper_bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "figures/precision_frontier.svg")
    parser.add_argument("--preview", type=Path, help="Optional PNG for local visual inspection")
    args = parser.parse_args()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "svg.fonttype": "none", "svg.hashsalt": "remote-gate-frontier-v1"})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.4), constrained_layout=True)
    blue, orange, pale = "#145D9B", "#B5531D", "#DCE8F1"
    p = np.linspace(4, 112, 433)
    low = np.array([lower_bound(32, 2.0**(-x))[0] for x in p])
    up = np.array([upper_bound(32, 2.0**(-x))[0] for x in p])
    axes[0].fill_between(p, low, up, color=pale, label="Unresolved interval")
    axes[0].plot(p, up, color=blue, lw=2.2, label="Achievable entropy bound")
    axes[0].plot(p, low, color=orange, lw=2.2, label="Converse bound")
    axes[0].plot(p, np.minimum(32, p / 2), color="#555555", ls="--", lw=1.2, label=r"Leading scale $m$")
    axes[0].set(title="Vary accuracy · 32-qubit target", xlabel=r"Accuracy bits $p=\log_2(1/\epsilon)$", ylabel="Entanglement of formation (ebits)", xlim=(4, 112), ylim=(0, 35))
    ns = np.arange(1, 49)
    low = np.array([lower_bound(int(n), 2.0**(-48))[0] for n in ns])
    up = np.array([upper_bound(int(n), 2.0**(-48))[0] for n in ns])
    axes[1].fill_between(ns, low, up, color=pale)
    axes[1].plot(ns, up, color=blue, lw=2.2)
    axes[1].plot(ns, low, color=orange, lw=2.2)
    axes[1].plot(ns, np.minimum(ns, 24), color="#555555", ls="--", lw=1.2)
    axes[1].axhline(1, color="#617F36", ls=":", lw=1.4)
    axes[1].text(47, 1.8, "One Bell pair with sequential messages", color="#486325", ha="right", fontsize=8.5)
    axes[1].set(title=r"Vary target size · $\epsilon=2^{-48}$", xlabel="Bob's target qubits n", xlim=(1, 48), ylim=(0, 28))
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#D7DCE0", lw=0.6)
        ax.set_axisbelow(True)
    axes[0].legend(frameon=False, loc="lower right", fontsize=8.5)
    fig.suptitle("Precision controls the entanglement price of one simultaneous exchange", fontsize=13, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None, "Creator": "verification/plot_frontier.py"})
    if args.preview:
        args.preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview, dpi=160)
    print(args.output)


if __name__ == "__main__":
    main()
