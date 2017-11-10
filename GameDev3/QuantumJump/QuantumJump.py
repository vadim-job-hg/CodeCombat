# Practice changing the positions of units.

# This function spawns 'type' at a point with a given x coordinate, and a random y coordinate.
def spawnRandomX(type, x):
    y = game.randomInteger(4, 64)
    game.spawnXY(type, x, y)

hero = game.spawnHeroXY("duelist", 6, 34)
hero.maxSpeed = 20

# This object will be our special fence.
game.spawnXY("fence", 40, 34)

spawnRandomX("munchkin", 12)
spawnRandomX("munchkin", 16)
spawnRandomX("munchkin", 20)
spawnRandomX("munchkin", 24)
spawnRandomX("munchkin", 28)
spawnRandomX("munchkin", 32)
spawnRandomX("scout", 48)
spawnRandomX("scout", 52)
spawnRandomX("scout", 56)
spawnRandomX("scout", 60)
spawnRandomX("scout", 64)
spawnRandomX("scout", 68)

# This configures properties for newly spawned ogres.
def onSpawn(event):
    unit = event.target
    unit.maxSpeed = 15
    unit.scale = 2

# This controls munchkin behavior.
def onUpdateMunchkin(event):
    unit = event.target
    # Our munchkins always move up.
    unit.moveXY(unit.pos.x, unit.pos.y + 5)
    # If the unit has moved beyond the top of the map.
    if unit.pos.y > 68:
        # Move it to the bottom of the map.
        unit.pos.y = 0

# This controls scout behavior.
def onUpdateScout(event):
    unit = event.target
    # Scouts always move down:
    unit.moveXY(unit.pos.x, unit.pos.y - 5)
    # If unit.pos.y is less than 0:
    if unit.pos.y<0:
        # Set its pos.y property to 68:
        unit.pos.y = 68

game.setActionFor("munchkin", "spawn", onSpawn);
game.setActionFor("scout", "spawn", onSpawn);
game.setActionFor("munchkin", "update", onUpdateMunchkin);
game.setActionFor("scout", "update", onUpdateScout);

# This function defines what happens when the player collides with something.
def onCollide(event):
    unit = event.target
    other = event.other
    # If other.type is "munchkin" or "scout".
    if other.type == "munchkin" or other.type == "scout":
        # The enemy's stomped the player.
        unit.defeat()
    # If other.type is "fence":
    if other.type == "fence":
        # Use unit.pos.x to change the player x coordinate.
        # Add 6 to the player's x position:
        hero.pos.x+=6

hero.on("collide", onCollide);

game.addMoveGoalXY(74, 34)
game.addSurviveGoal()