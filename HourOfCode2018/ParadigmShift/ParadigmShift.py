# Let's make a platformer game using game.setGravity()

# Set up the map with some platforms.
game.spawnFloor("mountain")
game.spawnTopBorder("desert")
game.spawnXY("forest", 10, 10)
game.spawnXY("forest", 18, 10)
game.spawnXY("forest", 36, 20)
game.spawnXY("forest", 44, 20)
game.spawnXY("forest", 76, 10)
game.spawnXY("forest", 20, 40)
game.spawnXY("forest", 28, 40)

# Spawn some gems to collect.
game.spawnXY("gold-coin", 20, 48)
game.spawnXY("gold-coin", 60, 40)
game.spawnXY("gold-coin", 75, 20)
game.spawnXY("gold-coin", 5, 40)

game.addSurviveGoal("raider")
game.addCollectGoal()

# Make the gravity pull down.
# This sets 0 gravity left/right, and 30 down.
game.setGravity(0, 30)

# Spawn the player and set her speed.
game.spawnXY("raider", 10, 18)
game.setPropertyFor("raider", "maxSpeed", 20)

# You can configure custom controls for your game.
# This makes the "raider" jump when space bar is pressed.
game.onKey("space", handler.jump(35, "raider"))
# This makes the "raider" move right when "d" is pressed.
game.onKey("d", handler.moveRight("raider"))
# Make it so the "raider" moves LEFT when "a" is pressed:
game.onKey("a", handler.moveLeft("raider"))

# handler.stop() stops movement.
# The "collide" event triggers a handler
# when one thing touches another thing.
# Set a "collide" action for "raider" to stop()
game.setActionFor("raider", "collide", handler.stop())
# handler.defeat() causes a unit to be defeated.
# The "exit" event triggers a handler
# when a unit exits the map.
# Set an "exit" action for "raider" to defeat()
game.setActionFor("raider", "exit", handler.defeat())
