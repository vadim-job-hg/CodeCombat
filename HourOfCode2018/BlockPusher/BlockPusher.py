# Push stone blocks carefully. Think before.

# Re-style of the level by changing the string "forest"
# Other options include "desert", "mountains", ...
game.spawnFloor("desert") # ∆
# Maze tiles could be any too. Change "forest" to "clump":
game.spawnMaze("clump", 8) # ∆

# The hero can be different.
game.spawnPlayerXY('goliath', 12, 12)
game.setPropertyFor("goliath", "maxSpeed", 20)

# Stone blocks are heavy, square and movable.
game.spawnXY("stone-block", 12, 20)
game.spawnXY("stone-block", 20, 12)
game.spawnXY("stone-block", 36, 44)
game.spawnXY("stone-block", 36, 28)
game.spawnXY("stone-block", 44, 60)
game.setPropertyFor("stone-block", "scale", 1.4)

# Collect all the gems to win
game.addCollectGoal()
game.spawnXY("gem", 44, 36)
game.spawnXY("gem", 52, 12)
game.spawnXY("gem", 60, 36)
game.spawnXY("gem", 12, 36)
