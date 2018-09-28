# Push boulders and collect all gems.

game.spawnFloor("forest")
game.spawnMaze("forest", 8)
game.spawnXY("forest", 44, 12)

# We need to create a player character.
game.spawnPlayerXY('captain', 12, 12)
game.setPropertyFor("captain", "maxSpeed", 20)

# Collect all the gems to win
game.addCollectGoal()

# The next line makes a new gem at {x:44, y:36}
game.spawnXY("gem", 44, 36)
game.spawnXY("gem", 52, 12)
# Add a gem at coordinates {x:60, y:36}
game.spawnXY("gem", 60, 36)
# Mouse over the playfield to find a place for another gem.
game.spawnXY("gem", 60, 52)
# Spawning and configuring bunch of boulders.
game.spawnXY("boulder", 12, 20)
game.spawnXY("boulder", 20, 12)
game.spawnXY("boulder", 36, 44)
game.spawnXY("boulder", 36, 28)
game.spawnXY("boulder", 44, 60)
game.setPropertyFor("boulder", "scale", 1.5)
