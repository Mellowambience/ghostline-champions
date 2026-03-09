#!/usr/bin/env python3
"""
Generate a themed game asset + UI pack for Ghostline-style projects.

Usage:
 python3 scripts/generate_game_pack.py
 python3 scripts/generate_game_pack.py --out game_pack
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent

THEME = {
    "name": "ghostline-mars",
    "palette": {
        "bg_0": "#13090b",
        "bg_1": "#2f111a",
        "bg_2": "#6f1f2a",
        "ink": "#f7e8d7",
        "muted": "#d9c5b3",
        "accent": "#f0533a",
        "accent_soft": "#ffc3a1",
        "line": "rgba(255, 222, 199, 0.28)",
        "good": "#7df5c3",
        "warn": "#ffd079",
        "bad": "#ff8a8a",
    },
}


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def tokens_css() -> str:
    p = THEME["palette"]
    return dedent(
        f"""
        :root {{
          --gh-bg-0: {p["bg_0"]};
          --gh-bg-1: {p["bg_1"]};
          --gh-bg-2: {p["bg_2"]};
          --gh-ink: {p["ink"]};
          --gh-muted: {p["muted"]};
          --gh-accent: {p["accent"]};
          --gh-accent-soft: {p["accent_soft"]};
          --gh-line: {p["line"]};
          --gh-good: {p["good"]};
          --gh-warn: {p["warn"]};
          --gh-bad: {p["bad"]};
          --gh-radius-sm: 10px;
          --gh-radius-md: 14px;
          --gh-radius-lg: 18px;
          --gh-shadow: 0 18px 40px rgba(0, 0, 0, 0.38);
          --gh-font-ui: "Space Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
          --gh-font-display: "Cinzel", Georgia, serif;
        }}
        """
    )


def components_css() -> str:
    return dedent(
        """
        @import url("https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Space+Mono:wght@400;700&display=swap");
        @import url("./tokens.css");

        .gh-root {
          color: var(--gh-ink);
          font-family: var(--gh-font-ui);
          background:
            radial-gradient(circle at 16% 12%, rgba(255, 195, 161, 0.22), transparent 46%),
            radial-gradient(circle at 84% 8%, rgba(240, 83, 58, 0.25), transparent 42%),
            linear-gradient(135deg, var(--gh-bg-0), var(--gh-bg-1) 45%, var(--gh-bg-2));
        }

        .gh-panel {
          background: rgba(15, 5, 7, 0.72);
          border: 1px solid var(--gh-line);
          border-radius: var(--gh-radius-lg);
          box-shadow: var(--gh-shadow);
          backdrop-filter: blur(5px);
        }

        .gh-title {
          margin: 0;
          font-family: var(--gh-font-display);
          letter-spacing: 0.05em;
          color: #ffe7d5;
        }

        .gh-subtitle {
          color: var(--gh-muted);
          font-size: 0.92rem;
        }

        .gh-btn {
          border: 1px solid var(--gh-line);
          border-radius: 12px;
          background: linear-gradient(130deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.02));
          color: var(--gh-ink);
          padding: 10px 12px;
          font: inherit;
          cursor: pointer;
          transition: 180ms ease;
        }

        .gh-btn:hover {
          border-color: rgba(255, 195, 161, 0.75);
          transform: translateY(-1px);
          background: linear-gradient(130deg, rgba(240, 83, 58, 0.22), rgba(255, 255, 255, 0.04));
        }

        .gh-bar {
          height: 10px;
          background: rgba(255, 255, 255, 0.12);
          border: 1px solid rgba(255, 255, 255, 0.18);
          border-radius: 999px;
          overflow: hidden;
        }

        .gh-bar > span {
          display: block;
          height: 100%;
        }

        .gh-bar.hp > span { background: linear-gradient(90deg, #f7d19d, #f0533a); }
        .gh-bar.en > span { background: linear-gradient(90deg, #a3f5d7, #66c9e2); }
        """
    )


def ux_flows_md() -> str:
    return dedent(
        """
        # Ghostline UX Flows

        ## Core Loop
        1. Start Run
        2. Review Champion Forecast
        3. Select Active Sigil
        4. Execute turn actions
        5. Resolve status + energy
        6. Intermission tuning (optional swap)
        7. Advance or fail and restart

        ## HUD Priorities
        - Keep HP and Energy visible at all times.
        - Show one high-contrast threat indicator before enemy burst turns.
        - Preserve move readability with type + cost + output in one line.

        ## UI Rules
        - Combat actions: minimum 44px touch target.
        - Critical state uses `--gh-bad`; avoid red for neutral labels.
        - Success moments use brief motion (120-300ms), no long delays.
        - Mobile layout stacks move cards into one column under 760px width.
        """
    )


def ui_schema_json() -> str:
    data = {
        "theme": THEME["name"],
        "screens": [
            {"id": "main_menu", "widgets": ["start_button", "run_history", "lore_tip"]},
            {
                "id": "battle",
                "widgets": ["player_status", "enemy_status", "move_grid", "battle_log", "threat_indicator"],
            },
            {"id": "intermission", "widgets": ["roster_swap", "heal_choice", "next_champion_preview"]},
        ],
        "hud": {
            "always_visible": ["hp_bar", "energy_bar", "shield_pill"],
            "conditional": ["critical_alert", "burst_warning"],
        },
    }
    return json.dumps(data, indent=2)


def readme_md(out_dir: Path) -> str:
    rel_out = out_dir.as_posix()
    return dedent(
        f"""
        # Ghostline Game Pack

        Generated assets, HUD templates, and UI/UX scaffolding for your battle game.

        ## Regenerate

        ```bash
        python3 scripts/generate_game_pack.py --out {rel_out}
        ```

        ## Contents
        - `ui/tokens.css` - design tokens.
        - `ui/components.css` - reusable HUD/GUI styles.
        - `ux/flows.md` - interaction flow guidance.
        - `data/ui_schema.json` - screen/widget map.
        - `manifest.json` - generation metadata and file index.
        """
    )


def generate(out_dir: Path) -> None:
    files: dict[str, str] = {}
    files["README.md"] = readme_md(out_dir)
    files["ui/tokens.css"] = tokens_css()
    files["ui/components.css"] = components_css()
    files["ux/flows.md"] = ux_flows_md()
    files["data/ui_schema.json"] = ui_schema_json()

    written = []
    for rel_path, content in files.items():
        path = out_dir / rel_path
        write_file(path, content)
        written.append(rel_path)

    manifest = {
        "name": "Ghostline Game Pack",
        "theme": THEME["name"],
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "file_count": len(written),
        "files": sorted(written),
    }
    write_file(out_dir / "manifest.json", json.dumps(manifest, indent=2))
    print(f"Generated {len(written) + 1} files in {out_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Ghostline game assets/HUD/UI pack.")
    parser.add_argument(
        "--out",
        default="game_pack",
        help="Output directory (default: game_pack)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_dir = Path(args.out).expanduser().resolve()
    generate(out_dir)


if __name__ == "__main__":
    main()