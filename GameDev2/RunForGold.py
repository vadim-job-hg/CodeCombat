# https://codecombat.com/play/level/run-for-gold?
# Generate randomly placed treasures and destroy them later.

# This spawns an item with lifetime at a random point.
def spawnValuable(itemType, lifetime):
    x = game.randomInteger(12, 68)
    y = game.randomInteger(12, 56)
    item = game.spawnXY(itemType, x, y)
    item.destroyTime = game.time + lifetime


# This spawns the treasure set.
def spawnTreasures():
    spawnValuable("bronze-coin", 6)
    spawnValuable("silver-coin", 5)
    spawnValuable("gold-coin", 4)
    spawnValuable("gem", 2)


# The event handler for items.
def onSpawn(event):
    item = event.target
    while True:
        # If the game time is greater than item destroyTime:
        if game.time >= item.destroyTime:
            # Destroy the item:
            item.destroy()
        pass


game.setActionFor("bronze-coin", "spawn", onSpawn)
game.setActionFor("silver-coin", "spawn", onSpawn)
game.setActionFor("gold-coin", "spawn", onSpawn)
game.setActionFor("gem", "spawn", onSpawn)

# Game settings, goals and UI.
game.spawnTime = 0
game.spawnInterval = 3
game.score = 0
if not db.get("topScore"):
    db.set("topScore", 0)
ui.track(game, "time")
ui.track(game, "score")
ui.track(db, "topScore")
goal = game.addManualGoal("Collect at least 50 gold for 30 seconds.")

# The hero setup.
hero = game.spawnHeroXY("captain", 40, 34)
hero.maxSpeed = 25


def onCollect(event):
    item = event.other
    # If the item has 'value' property:
    if item.value:
        # Increase the game score by item's value:
        game.score += item.value


hero.on("collect", onCollect)


# This checks timers for treasure spawning.
def checkSpawns():
    # If game time is greater than game spawnTime:
    if game.time > game.spawnTime:
        # Use spawnTreasures to create more items.
        spawnTreasures()
        # Increase game.spawnTime by game.spawnInterval:
        game.spawnTime += game.spawnInterval
    pass


# This checks the goal state.
def checkGoal():
    if game.score > 50:
        goal.success = True
    else:
        goal.success = False


# This checks the game state.
def checkGameOver():
    if game.time > 30:
        checkGoal()
        db.set("topScore", game.score)


while True:
    checkSpawns()
    checkGameOver()
