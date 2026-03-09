# Ghostline Champions — Game Design Document

### A Monster-Bonding RPG Inspired by Classic Creature Collectors

---

## Overview

**Ghostline Champions** is a turn-based monster-bonding RPG inspired by classic creature-collecting games such as Pokémon Yellow and Pokémon Crystal.

The goal is not to copy those games, but to capture the feeling they created:
- exploration
- mysterious creatures
- bonding with a team
- strategic battles
- a strange and memorable world

Ghostline Champions introduces its own identity through **emotion-driven evolution**, **bond mechanics**, and **living echoes called Ghostlines**.

---

## Core Pillars

### 1. Exploration
The world rewards curiosity. Players discover rare Ghostlines, hidden items, environmental lore, and secret paths across forests, caves, ruins, and cities. Exploration feels relaxing and mysterious rather than overwhelming.

### 2. Creature Bonding
Ghostlines are not animals. They are **emotional echoes of the world** — each creature represents a memory, event, or force within the environment. Players don't simply capture them — they **attune to them**. Bonding increases power and unlocks hidden forms.

### 3. Strategic Battles
Turn-based and tactical. Players choose between attacking, bonding, swapping Ghostlines, and using items. Easy to learn, difficult to master.

### 4. A Living World
The world contains factions, ruins, strange phenomena, and champions. Players slowly uncover the mystery behind Ghostlines and their origin.

---

## Core Gameplay Loop

```
Explore region → Encounter Ghostline → Battle or bond → Add to roster
→ Train and evolve → Challenge regional champions → Unlock new areas → Discover deeper lore
```

---

## Ghostlines (Creatures)

Ghostlines are living echoes formed from strong memories or forces within the world.

| Name | Type | Theme |
|---|---|---|
| Ember Wisp | Ember | fire spirit |
| Moss Sentinel | Moss | forest guardian |
| Static Pup | Static | electrical energy |
| Tide Serpent | Tide | ocean current |
| Lunar Moth | Astral | dream entity |

---

## Evolution System

Evolution occurs through:
- **Level Growth** — traditional leveling
- **Bond Level** — higher emotional connection unlocks transformations
- **Environmental Triggers** — certain locations trigger rare evolutions
- **Champion Sigils** — defeating champions unlocks advanced evolution paths

Example evolution tree:
```
Wisp → Ember Wisp → Solar Phantom
     → Ash Wisp   → Void Lantern
```

---

## Elemental Type System

| Type | Strong Against |
|---|---|
| Ember | Moss |
| Moss | Stone |
| Stone | Static |
| Static | Tide |
| Tide | Ember |
| Spectral | rare universal |

---

## Bond System

Players perform a **Bond Pulse** instead of simple capture. Bond success depends on:
- creature health
- player bond level
- environmental resonance

Higher bonds unlock: stat bonuses, hidden abilities, alternate evolutions, cosmetic variants.

---

## Champion System

Champions are powerful trainers who protect each region. Defeating a champion grants a **Champion Sigil**.

Sigils unlock: new evolution paths, restricted zones, rare Ghostline encounters.

| Champion | Region Theme |
|---|---|
| Flora Warden | forest |
| Storm Rider | coastal storms |
| Obsidian Knight | volcanic mountains |
| Neon Architect | futuristic city |

---

## World Structure

### Verdant Hollow
Ancient forest region. Ruins, moss creatures, early tutorial area.

### Static Coast
Storm-covered islands. Shipwrecks, lightning towers, rare static Ghostlines.

### Obsidian Range
Volcanic mountain region. Magma caverns, dangerous terrain, powerful Ember creatures.

### Lumen City
Futuristic metropolis built around Ghostline research. Labs, markets, faction conflicts.

### Astral Basin
Surreal dream-like endgame region where reality becomes unstable.

---

## Battle System

Turn-based combat. Player commands: **Attack / Bond / Item / Swap**

```
Start battle → Choose action → Resolve turn order → Apply damage or effects → Repeat
```

---

## Creature Stats

`HP · Attack · Defense · Focus · Speed · Bond`

Bond determines evolution potential and ability strength.

---

## Abilities

Examples: Ember Burst · Static Pulse · Moss Shield · Tide Surge · Astral Blink

Abilities include: damage attacks, buffs, status effects, terrain manipulation.

---

## Items

Potion · Revive Seed · Bond Charm · Element Orb · Evolution Catalyst

---

## Technical Stack

**Engine**: Godot (strong 2D support, open source, lightweight, easy scripting)  
**Language**: GDScript / C#

---

## Repository Structure

```
ghostline-champions/
├── assets/        sprites · tiles · audio
├── creatures/     ghostlines · evolutions · abilities
├── world/         regions · towns · dungeons
├── battle/        combat_engine · ai
├── champions/
├── ui/
└── story/
```

---

## Minimum Viable Game

1 region · 10 Ghostlines · 3 towns · 1 dungeon · 2 champions · basic battle system

---

## Long Term Goals

- Expanded creature roster
- Multiplayer trading
- Procedural Ghostline variants
- Community modding support
- Cross-platform release

---

## Vision

Ghostline Champions should feel like discovering a lost classic RPG from an alternate timeline.  
A game that respects the past while creating its own mythology.  
The goal is not imitation. The goal is **wonder**.
