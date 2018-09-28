# Click 'Test Level' button and win the level.
# 'A' -- move to left; 'D' -- move to right.

# Creating walls and the floor.
game.spawnFloor("forest")
game.spawnLeftBorder("forest")
game.spawnRightBorder("forest")
game.spawnTopBorder("forest")

# The movable paddle.
game.spawnXY("platform", 38, 10)
game.setPropertyFor("platform", "maxSpeed", 50)
# The paddle can collect items which score 50 points.
game.setPropertyFor("platform", "collects", True)
game.setActionFor("platform", "collect", handler.addScore(50))
# Setting the control.
game.onKey("A", handler.moveLeft("platform"))
game.onKey("D", handler.moveRight("platform"))

# The flying ball.
game.spawnXY("flying-ball", 40, 30)
game.setPropertyFor("flying-ball", "maxSpeed", 30)
game.setPropertyFor("flying-ball", "rotation", 0.8)
# On a hit, the ball defeats targets and scores a point.
game.setActionFor("flying-ball", "collide", handler.defeatOther())
game.setActionFor("flying-ball", "collide", handler.addScore(1))
# Each lost ball returns back and costs 20 points.
game.setActionFor("flying-ball", "exit", handler.teleportTo(40, 40))
game.setActionFor("flying-ball", "exit", handler.addScore(-20))

# Double size robots score 100 points when defeated.
game.spawnXY("robobomb", 20, 48)
game.spawnXY("robobomb", 30, 52)
game.spawnXY("robobomb", 50, 52)
game.spawnXY("robobomb", 60, 48)
game.setPropertyFor("robobomb", "scale", 2)
game.setActionFor("robobomb", "defeat", handler.addScore(100))

# Invisible generators spawn gems in 10 meters range.
game.spawnXY("generator", 30, 58)
game.spawnXY("generator", 50, 58)
game.setPropertyFor("generator", "visible", False)
game.setPropertyFor("generator", "spawnType", "gem")
game.setPropertyFor("generator", "spawnRadius", 10)

# Gems move down constantly and disappear out the screen.
game.setPropertyFor("gem", "maxSpeed", 25)
game.setActionFor("gem", "update", handler.moveDown())
game.setActionFor("gem", "exit", handler.destroy())

ui.track(game, "score")
# Setting the game goal and directions for players.
game.addDefeatGoal()
