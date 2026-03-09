class_name BattleAI
extends Node

enum Difficulty { PASSIVE, STANDARD, AGGRESSIVE }

static func pick_ability(enemy: Dictionary, player: Dictionary, difficulty: int = Difficulty.STANDARD) -> Dictionary:
	var affordable = []
	for ab in enemy["abilities"]:
		if enemy["focus"] >= ab.get("focus_cost", 0):
			affordable.append(ab)
	if affordable.is_empty():
		return {}
	var hp_pct = float(enemy["hp"]) / float(enemy["max_hp"])
	if hp_pct < 0.4:
		var heals = affordable.filter(func(a): return a.get("category") == "heal" or a.get("category") == "drain")
		if not heals.is_empty():
			return heals[0]
	match difficulty:
		Difficulty.PASSIVE:
			affordable.sort_custom(func(a, b): return a.get("focus_cost", 0) < b.get("focus_cost", 0))
			return affordable[0]
		Difficulty.AGGRESSIVE:
			var attacks = affordable.filter(func(a): return a.get("category") == "attack")
			if not attacks.is_empty():
				attacks.sort_custom(func(a, b): return a.get("power", 0) > b.get("power", 0))
				return attacks[0]
			return affordable[randi() % affordable.size()]
		_:
			return affordable[randi() % affordable.size()]
