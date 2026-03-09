# Getting Started (Godot 4.x)

## 1. Install Godot
Download **Godot 4.2+** from https://godotengine.org/download  
Use the **Standard** build (not .NET unless you want C#).

## 2. Open the project
1. Launch Godot
2. Click **Import**
3. Navigate to `ghostline-champions/godot/`
4. Select `project.godot`
5. Click **Import & Edit**

## 3. Project structure

```
godot/
├── project.godot          ← Godot project file
├── main.gd                ← Entry point
├── scenes/                ← .tscn scene files (create as you build)
│   ├── main_menu.tscn
│   ├── overworld.tscn
│   └── battle.tscn
├── creatures/
│   ├── ghostline_data.gd  ← Resource schema
│   ├── roster.json        ← All 10 starter Ghostlines
│   ├── abilities.json     ← Full ability registry
│   └── type_chart.gd      ← Type multiplier lookup
├── battle/
│   ├── battle_engine.gd   ← Damage, turn order, bond pulse, evolution check
│   └── battle_ai.gd       ← Enemy decision logic (3 difficulty modes)
├── world/
│   └── regions.json       ← 5 regions with unlock conditions
├── champions/
│   └── champions.json     ← 4 champions with full teams
├── story/
│   └── player_state.gd    ← Save/load schema
└── assets/                ← sprites/, tiles/, audio/ (populate as you build)
```

## 4. First scenes to build (MVG order)

| Priority | Scene | What it does |
|---|---|---|
| 1 | `battle.tscn` | Core loop — plugs directly into battle_engine.gd |
| 2 | `main_menu.tscn` | Start screen, load save |
| 3 | `overworld.tscn` | Movement, grass encounters, town entry |
| 4 | `bond_pulse.tscn` | Bond Pulse UI — replaces capture mechanic |
| 5 | `evolution.tscn` | Evolution cutscene + stat transition |

## 5. Loading creature data

```gdscript
var roster_json = FileAccess.open("res://creatures/roster.json", FileAccess.READ)
var ghostlines = JSON.parse_string(roster_json.get_as_text())
```

## 6. Running the battle engine

```gdscript
var damage = BattleEngine.calculate_damage(
  player_level,
  player_attack,
  enemy_defense,
  ability_power,
  ability_type,   # e.g. "Ember"
  enemy_type      # e.g. "Moss"
)
# → returns int, includes type multiplier + random variance
```

## 7. MVG checkpoint
The browser `index.html` demo validates the battle loop and visual language.  
The Godot build starts above that: overworld movement, creature encounters, Bond Pulse, save state.

---

*"A game that respects the past while creating its own mythology."*
