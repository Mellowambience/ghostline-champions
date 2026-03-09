# Ghostline Champions

Standalone game prototype and UI asset pipeline inspired by champion battle formats, themed around AetherRose / Ghostline lore.

## Contents
- `index.html` - playable Ghostline Champions prototype.
- `game_pack/` - generated HUD/GUI/UI assets and UX docs.
- `scripts/generate_game_pack.py` - asset/UI generator.
- `research.md` - design and source notes.

## Run Locally
```bash
cd /Users/torty/ghostline-champions
python3 -m http.server 8080
```
Then open [http://localhost:8080](http://localhost:8080).

## Regenerate Game Pack
```bash
python3 scripts/generate_game_pack.py --out game_pack
```
