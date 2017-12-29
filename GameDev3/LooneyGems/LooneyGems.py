#  Why should gems wait while you are collecting them?

# This spawns a gem at a random point with random directions
def spawnRandomGem():
    x = game.randomInteger(10, 70)
    y = game.randomInteger(10, 58)
    gem = game.spawnXY("gem", x, y)
    # This defines the direction by X axis.
    gem.dirX = game.randomInteger(-1, 1)
    # This defines the direction by Y axis.
    gem.dirY = game.randomInteger(-1, 1)
    gem.scale = 1.5

# Spawn as many gems as you want.
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()

gemSpeed = 1.2

# This handler moves gems.
def onUpdate(event):
    item = event.target
    # There are two parts of moving: X and Y.
    diffX = item.dirX * gemSpeed
    diffY = item.dirY * gemSpeed
    # Increase item.pos.x by diffX:
    item.pos.x += diffX
    # Increase item.pos.y by diffY:
    item.pos.y += diffY
    # If the item is out of boundd by the X coordinate.
    if item.pos.x > 70 or item.pos.x < 10:
        # Then we change X direction for the item.
        item.dirX *= -1
    # If item.pos.y greater than 58 or less than 10:
    if item.pos.y > 58 or item.pos.y < 10:
        # Multiply item.dirY by -1:
        item.dirY *= -1

game.setActionFor("gem", "update", onUpdate)

hero = game.spawnHeroXY("captain", 40, 34)
hero.maxSpeed =20
game.addCollectGoal()
ui.track(game, "time")