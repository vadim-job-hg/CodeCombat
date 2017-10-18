# https://codecombat.com/play/level/lernaean-hydra
# For each defeated ogres we should create two new ogres.

player = game.spawnHeroXY("knight", 40, 34)
player.attackDamage = 20

# Lets count defeated and how many to defeat.
game.defeated = 0
game.toDefeat = 16
game.addDefeatGoal(game.toDefeat)
# We're tracking important for the current level variables.
ui.track(player, "health")
ui.track(game, "defeated")
ui.track(game, "toDefeat")

# Starter enemies.
game.spawnXY("munchkin", 30, 14)
game.spawnXY("munchkin", 50, 54)

# It makes new enemies aggresive.
def onSpawn(event):
    unit = event.target
    unit.behavior = "AttacksNearest"

# It tracks and count defeated enemies.
def onDefeat(event):
    unit = event.target
    # One enemy to victory is less.
    game.toDefeat -= 1
    # Increase the game's defeated property:
    game.defeated +=1
    # Coordinates for new enemies.
    x1 = game.randomInteger(10, 40)
    x2 = game.randomInteger(40, 70)
    y = game.randomInteger(12, 56)
    game.spawnXY("potion-small", unit.pos.x, unit.pos.y)
    # Spawn two "munchkin"s at points {x1, y} and {x2, y}:
    game.spawnXY("munchkin", x1, y)
    game.spawnXY("munchkin", x2, y)

game.setActionFor("munchkin", "spawn", onSpawn)
# Set the "munchkin"'s event handler for the "defeat" event:
game.setActionFor("munchkin", "defeat", onDefeat)
