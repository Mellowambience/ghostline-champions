class_name PlayerState
extends Resource

@export var player_name: String = "Amara\u2234"
@export var bond_level: int = 0
@export var sigils: Array[String] = []
@export var regions_unlocked: Array[String] = ["verdant_hollow"]
@export var current_region: String = "verdant_hollow"
@export var roster: Array[Dictionary] = []
@export var active_index: int = 0
@export var items: Dictionary = { "potion": 3, "bond_charm": 1 }
@export var play_time_seconds: int = 0
@export var ghostlines_bonded: Array[String] = []
@export var champions_defeated: Array[String] = []

func save_to_file(path: String) -> void:
	ResourceSaver.save(self, path)

static func load_from_file(path: String) -> PlayerState:
	if ResourceLoader.exists(path):
		return ResourceLoader.load(path) as PlayerState
	return PlayerState.new()
