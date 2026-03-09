# Type multiplier lookup
# Usage: TypeChart.get(attacker_type, {}).get(defender_type, 1.0)

const TYPE_CHART = {
  "Ember":    { "Moss": 2.0, "Tide": 0.5 },
  "Moss":     { "Stone": 2.0, "Ember": 0.5 },
  "Stone":    { "Static": 2.0, "Moss": 0.5 },
  "Static":   { "Tide": 2.0, "Stone": 0.5 },
  "Tide":     { "Ember": 2.0, "Static": 0.5 },
  "Spectral": {},
  "Astral":   {}
}
# Spectral: 1.2x universal, 0.5x vs Spectral, 1.5x vs Astral
# Astral:   1.5x vs Spectral, 0.5x vs Astral, 1.0x all others
