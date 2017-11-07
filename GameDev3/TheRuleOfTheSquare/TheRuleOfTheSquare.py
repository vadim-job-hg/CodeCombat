# Use the new event "update" for units' logic.

# It spawns type0 or type1 unit at a {x, random} point.
def spawnRandomUnit(x, type0, type1):
    typeNumber = game.randomInteger(0, 1)
    y = game.randomInteger(12, 56)
    if typeNumber == 0:
        game.spawnXY(type0, x, y)
    else:
        game.spawnXY(type1, x, y)


# It compares types and decides
# whether the target should be attacked.
def shouldAttack(who, target):
    # "scout" doesn't like "soldier".
    if who.type == "scout" and target.type == "soldier":
        return True
    # "soldier" doesn't like "thrower".
    if who.type == "soldier" and target.type == "thrower":
        return True
    # "thrower" doesn't like "archer".
    if who.type == "thrower" and target.type == "archer":
        return True
    # "archer" doesn't like "scout".
    if who.type == "archer" and target.type == "scout":
        return True


# The event handler for units for the "update" event.
def onUpdateUnit(event):
    unit = event.target
    enemy = unit.findNearestEnemy()
    if enemy and shouldAttack(unit, enemy):
        unit.attack(enemy)
    else:
        # Ogres move to the left, humans to the right.
        if unit.team == "ogres":
            unit.moveXY(unit.pos.x - 3, unit.pos.y)
        else:
            # Move the unit to the left:

            pass
    # We don't need units which are outside of the screen.
    if unit.pos.x > 80 or unit.pos.x < 0:
        unit.destroy()


# We're using one event handler for all units.
game.setActionFor("thrower", "update", onUpdateUnit)
game.setActionFor("scout", "update", onUpdateUnit)
# Set the "update" event handler for "archer" and "soldier":
game.setActionFor("archer", "update", onUpdateUnit)
game.setActionFor("soldier", "update", onUpdateUnit)

game.interval = 2
game.spawnTime = 0
game.addDefeatGoal(10)


# It works as "game loop" from previous levels.
def onUpdateGame(event):
    if game.time > game.spawnTime:
        game.spawnTime += game.interval
        spawnRandomUnit(2, "archer", "soldier")
        spawnRandomUnit(78, "thrower", "scout")


# Each time frame we call onUpdateGame function.
game.on("update", onUpdateGame)
