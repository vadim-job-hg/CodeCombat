# Click to robots to protect the peasant.

game.spawnFloor("glacier")
game.spawnTopBorder("glacier")
game.spawnBottomBorder("glacier")
game.spawnDecorations("glacier", 2)

# We can place generators out of the screen.
game.spawnXY("generator", -10, 34)
game.spawnXY("generator", 90, 34)
game.spawnXY("peasant", 40, 34)
# Coins and potions are collectables.
game.spawnRandomly("gold-coin", 20)
game.spawnRandomly("potion-large", 4)

# The peasant should collect coins.
game.setPropertyFor("peasant", "behavior", "Collects")
# The peasant should be big and healthy.
game.setPropertyFor("peasant", "scale", 2)
# Set "peasant"'s property "maxHealth" to 5000 at least:
game.setPropertyFor("peasant", "maxHealth", 5000)

# Configuring generators and robots.
game.setPropertyFor("generator", "spawnType", "robobomb")
game.setPropertyFor("generator", "spawnRadius", 10)
game.setPropertyFor("robobomb", "scale", 2)

# Instead of defeating we can damage enemies on "click".
game.on("click", handler.takeDamageOther(100))
# Score points make the game more competitive.
# Collecting event handler for peasants.
game.setActionFor("peasant", "collect", handler.addScore(50))
# Set for "robobomb"s' event "defeat" the handler addScore:
game.setActionFor("robobomb", "defeat", handler.addScore(100))

# The survive goal can be defined for specific units.
game.addSurviveGoal("peasant")
game.addScoreGoal(1500)

ui.track(game, "score")
