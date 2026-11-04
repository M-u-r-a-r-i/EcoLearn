"""Render lesson graphs from data specs, in one house style.

    venv\\Scripts\\python.exe scripts\\render_graphs.py            # every spec
    venv\\Scripts\\python.exe scripts\\render_graphs.py path.graph.yaml

Each `data/media/figures/<concept_id>/<name>.graph.yaml` becomes `<name>.svg`
next to it. Graphs are specs, not drawings, so the plotted line can never
disagree with its own data — the numbers in the spec ARE the graph.

Spec format (one panel, or up to two side by side under `panels:`):

    title: optional figure title
    panels:
      - title: optional panel title
        x: {label: "Current $I$ (mA)", min: 0, max: 320}
        y: {label: "Voltage $V$ (V)", min: 0, max: 7}
        series:
          - label: Resistor (ohmic)
            points: [[0, 0], [300, 6]]
            color: blue            # blue | red | green | orange | purple | gray
            style: solid           # solid | dashed | dotted
            markers: false
        marks:                     # labelled points
          - {x: 150, y: 6, text: "lamp at 6 V", color: red}
        legend: below              # optional: "below" (outside the plot) or any
                                   # matplotlib location, e.g. "upper left"

Labels use matplotlib mathtext, so `$V$` and `$\\Omega$` work.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import yaml  # noqa: E402

_ROOT = Path(__file__).resolve().parents[1]
FIGURES = _ROOT / "data" / "media" / "figures"

COLORS = {
    "blue": "#2563eb", "red": "#dc2626", "green": "#16a34a",
    "orange": "#ea580c", "purple": "#7c3aed", "gray": "#6b7280",
}
STYLES = {"solid": "-", "dashed": "--", "dotted": ":"}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#e5e7eb",
    "grid.linewidth": 0.8,
    "axes.edgecolor": "#374151",
    "axes.labelcolor": "#111827",
    "xtick.color": "#374151",
    "ytick.color": "#374151",
    "svg.hashsalt": "ecolearn",   # deterministic ids -> clean git diffs
})


def _panel(ax, spec: dict) -> None:
    for s in spec.get("series", []):
        xs, ys = zip(*s["points"])
        ax.plot(xs, ys,
                STYLES.get(s.get("style", "solid"), "-"),
                color=COLORS.get(s.get("color", "blue"), s.get("color", "blue")),
                linewidth=2.4,
                marker="o" if s.get("markers") else None,
                markersize=5,
                label=s.get("label"))
    for m in spec.get("marks", []):
        color = COLORS.get(m.get("color", "gray"), m.get("color", "gray"))
        ax.plot([m["x"]], [m["y"]], "o", color=color, markersize=7, zorder=5)
        ax.annotate(m["text"], (m["x"], m["y"]), textcoords="offset points",
                    xytext=m.get("offset", [8, 8]), color=color, fontsize=10)
    x, y = spec["x"], spec["y"]
    ax.set_xlabel(x["label"])
    ax.set_ylabel(y["label"])
    if "min" in x or "max" in x:
        ax.set_xlim(x.get("min"), x.get("max"))
    if "min" in y or "max" in y:
        ax.set_ylim(y.get("min"), y.get("max"))
    if spec.get("title"):
        ax.set_title(spec["title"], fontsize=12, color="#111827")
    if any(s.get("label") for s in spec.get("series", [])):
        where = spec.get("legend", "best")
        if where == "below":  # outside the axes: can never cover the data
            ax.legend(frameon=False, fontsize=10, loc="upper center",
                      bbox_to_anchor=(0.5, -0.16))
        else:
            ax.legend(frameon=False, fontsize=10, loc=where)


def render(spec_path: Path) -> Path:
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    panels = spec.get("panels") or [spec]
    if not 1 <= len(panels) <= 2:
        raise ValueError(f"{spec_path}: 1 or 2 panels supported, got {len(panels)}")
    fig, axes = plt.subplots(1, len(panels), figsize=(5.6 * len(panels), 4.0))
    axes = [axes] if len(panels) == 1 else list(axes)
    for ax, panel in zip(axes, panels):
        _panel(ax, panel)
    if spec.get("title") and spec.get("panels"):
        fig.suptitle(spec["title"], fontsize=13, color="#111827")
    fig.patch.set_facecolor("white")   # readable on dark-mode pages too
    fig.tight_layout()
    out = spec_path.with_name(spec_path.name.replace(".graph.yaml", ".svg"))
    fig.savefig(out, format="svg", metadata={"Date": None})
    plt.close(fig)
    return out


def main(argv: list[str]) -> int:
    # resolve(): relative paths from the command line must still sit under _ROOT
    # for the relative_to() in the report line below.
    specs = [Path(a).resolve() for a in argv] or sorted(FIGURES.glob("**/*.graph.yaml"))
    for spec in specs:
        out = render(spec)
        print(f"rendered {out.relative_to(_ROOT)}  ({out.stat().st_size // 1000} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
