# Defeat robots by clicking on them.

game.spawnFloor("mountain")
game.spawnDecorations("mountain", 19)

# "generator" produces new units or items.
game.spawnXY("generator", 40, 34)
game.setPropertyFor("generator", "visible", False)
game.setPropertyFor("generator", "spawnType", "robobomb")
game.setPropertyFor("generator", "spawnRadius", 20)
# By default "generator" spawns new unit every 5 seconds.
# It's slow. Set "spawnDelay" property to 2 or less:
game.setPropertyFor("generator", "spawnDelay", 2)

# Making robots big and wandering.
game.setPropertyFor("robobomb", "behavior", "Scampers")
game.setPropertyFor("robobomb", "scale", 2)
# You can set an event handler for units of the same type.
# Any "robobomb" will be destroyed out of the screen.
game.setActionFor("robobomb", "exit", handler.destroy())
# Defeated robots should give score points.
# Use game.setActionFor for "robobomb" type, "defeat" event
# and with handler.addScore(10)
game.setActionFor("robobomb", "defeat",  handler.addScore(10) )
# This method sets an event handler on the event "click".
# When you click on a unit it will be defeated.
game.on("click", handler.defeatOther())
# For each click you lose one score point.
game.on("click", handler.addScore(-1))

ui.track(game, "score")
# The goal of this level is getting 100 score points.
game.addScoreGoal(100)

