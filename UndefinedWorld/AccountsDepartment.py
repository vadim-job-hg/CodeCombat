# https://codecombat.com/play/level/accounts-department
# Setup characters.
hero = game.spawnHeroXY("captain", 40, 34)
hero.maxSpeed = 20
generator1 = game.spawnXY("generator", 4, 34)
generator2 = game.spawnXY("generator", 76, 34)
generator1.spawnDelay = 7
generator2.spawnDelay = 7
requiredScore
# Chests of gems are most valuable items.
game.spawnXY("chest", 68, 56)
game.spawnXY("chest", 14, 14)

# This function spawn a random item in a random place.
def spawnRandomItem():
    itemNumber = game.randomInteger(1, 3)
    x = game.randomInteger(12, 68)
    y = game.randomInteger(12, 56)
    if itemNumber == 1:
        game.spawnXY("bronze-coin", x, y)
    elif itemNumber == 2:
        game.spawnXY("gold-coin", x, y)
    elif itemNumber == 3:
        game.spawnXY("gem", x, y)

itemInterval = 1
itemSpawnTime = 0

def checkSpawnTimer():
    if game.time >= itemSpawnTime:
        spawnRandomItem()
        itemSpawnTime += itemInterval

# It allows to track and act for collected items.
def onCollect(event):
    # "event" parameter contains data about the collector.
    collector = event.target
    # And about the collected item.
    item = event.other
    if item.value:
        # Increase the game score by the item's value:
        game.score += item.value
        pass

# Assign onCollect handler for "hero" on "collect" event.
hero.on("collect", onCollect)

# Setup the goals and UI.
endTime = 30
# How many score points the player should get.
requiredScore = 250
goldGoal = game.addManualGoal('Collect at least 250 gold in 30 seconds.')
ui.track(game, "score")
ui.track(game, "time")

def checkGoals():
    if game.time >= endTime:
        # If game score is greater or equal requiredScore:
        if game.score>=requiredScore:
            # The game goal is succesful:
            goldGoal.success = True
        # Else it's failed:
        else:
            goldGoal.success = False
        pass

while True:
    checkSpawnTimer()
    checkGoals()
