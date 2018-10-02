# Now let's make a side-scrolling platformer.

game.spawnFloor("mountain")
game.spawnTopBorder("desert")

# Make sure the platforms don't fall off the map!
game.setPropertyFor("forest", "ignoreGravity", True)
game.setPropertyFor("gold-coin", "ignoreGravity", True)

# We don't want the platforms to scroll too fast!
game.setPropertyFor("forest","maxSpeed", 5)
game.setPropertyFor("gold-coin","maxSpeed", 10)

game.spawnXY("forest", 10, 10)
game.spawnXY("forest", 18, 10)
game.spawnXY("forest", 40, 20)
game.spawnXY("forest", 48, 20)
game.spawnXY("forest", 76, 10)
game.spawnXY("forest", 20, 40)
game.spawnXY("forest", 28, 40)

game.addSurviveGoal("duelist")
game.addCollectGoal(10)

# Make the gravity pull down.
game.setGravity(0, 30)

# Spawn the player and set his speed.
game.spawnXY("duelist", 10, 18)
game.setPropertyFor("duelist", "maxSpeed", 20)

# Configure custom controls.
game.onKey("space", handler.jump(35, "duelist"))
game.onKey("d", handler.moveRight("duelist"))
game.onKey("a", handler.moveLeft("duelist"))

game.setActionFor("duelist", "collide", handler.stop())
game.setActionFor("duelist", "exit", handler.defeat())

# Spawn coins randomly this time.
game.spawnXY("generator", 40, 35)
game.setPropertyFor("generator", "spawnType", "gold-coin")
game.setPropertyFor("generator", "spawnRadius", "30")
game.setPropertyFor("generator", "spawnDelay", 1)
game.setPropertyFor("generator", "visible", False)

# The "update" event is called continuously.
# Set an action for "forest"s to moveLeft() on "update".
game.setActionFor("forest", "update", handler.moveLeft())
# Set bounds to "warp" to make the platforms wrap around.
game.setBounds("warp")
# For extra fun, try making the coins move...
