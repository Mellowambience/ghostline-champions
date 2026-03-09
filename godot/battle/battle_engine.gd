class_name BattleEngine
extends Node

const TYPE_CHART = {
  "Ember":    { "Moss": 2.0, "Tide": 0.5 },
  "Moss":     { "Stone": 2.0, "Ember": 0.5 },
  "Stone":    { "Static": 2.0, "Moss": 0.5 },
  "Static":   { "Tide": 2.0, "Stone": 0.5 },
  "Tide":     { "Ember": 2.0, "Static": 0.5 },
  "Spectral": {},
  "Astral":   {}
}

static func get_type_multiplier(attacker_type: String, defender_type: String) -> float:
	if attacker_type == "Spectral":
		return 0.5 if defender_type == "Spectral" else 1.5 if defender_type == "Astral" else 1.2
	if attacker_type == "Astral":
		return 0.5 if defender_type == "Astral" else 1.5 if defender_type == "Spectral" else 1.0
	var chart = TYPE_CHART.get(attacker_type, {})
	return chart.get(defender_type, 1.0)

static func calculate_damage(
	attacker_level: int, attacker_attack: int, defender_defense: int,
	ability_power: int, attacker_type: String, defender_type: String
) -> int:
	var base = ((2.0 * attacker_level / 5.0 + 2.0) * ability_power * attacker_attack / defender_defense / 50.0 + 2.0)
	var type_mult = get_type_multiplier(attacker_type, defender_type)
	var random_mult = randf_range(0.85, 1.0)
	return int(base * type_mult * random_mult)

static func player_goes_first(player_speed: int, enemy_speed: int, player_priority: int = 0, enemy_priority: int = 0) -> bool:
	if player_priority != enemy_priority:
		return player_priority > enemy_priority
	if player_speed != enemy_speed:
		return player_speed > enemy_speed
	return randf() > 0.5

static func resolve_bond_pulse(ghostline_hp_pct: float, player_bond_level: int, environment_resonance: float) -> Dictionary:
	var base_chance = 0.3
	base_chance += (1.0 - ghostline_hp_pct) * 0.4
	base_chance += player_bond_level / 200.0
	base_chance *= environment_resonance
	base_chance = clamp(base_chance, 0.05, 0.95)
	var success = randf() < base_chance
	return { "success": success, "bond_delta": 8 if success else 2 }

static func check_evolution(ghostline: Dictionary) -> String:
	for evo in ghostline.get("evolutions", []):
		match evo["trigger"]:
			"level":       if ghostline["level"] >= evo["value"]: return evo["into"]
			"bond":        if ghostline["bond"] >= evo["value"]:  return evo["into"]
			"environment": if ghostline.get("current_env", "") == evo["value"]: return evo["into"]
			"sigil":       if ghostline.get("sigil_count", 0) >= evo["value"]:  return evo["into"]
	return ""
