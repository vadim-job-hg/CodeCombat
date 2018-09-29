# Just survive for 15 seconds.
# Use mouse clicking or "WASD" to control the hero.

game.spawnFloor("desert")
# You can spawn borders for required sides only.
game.spawnLeftBorder("forest")
game.spawnRightBorder("desert")
# This spawns a set of decorations with desert style.
game.spawnDecorations("desert", 42)
# Spawn more decorations with a different seed (not 42!):
game.spawnDecorations("desert", 1)
# "warp" bounds loop the game field.
game.setBounds("warp")

# Goliaths are strong but slow by default.
game.spawnPlayerXY("goliath", 42, 36)
# Use setPropertyFor to set "goliath" maxSpeed greater than 15:
game.setPropertyFor("goliath", "maxSpeed", 20)

# Wandering around robobombs.
game.spawnRandomly("robobomb", 16, 13)
game.setPropertyFor("robobomb", "maxSpeed", 1)
game.setPropertyFor("robobomb", "behavior", "Scampers")

# The number defines how long your hero should survive.
game.addSurviveGoal(15)
