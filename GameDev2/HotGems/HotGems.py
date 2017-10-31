# https://codecombat.com/play/level/hot-gems

# Gold should healthen you, gems should hurts you.

player = game.spawnHeroXY("captain", 40, 34)
player.maxSpeed = 20
# We're using relative health value for gems/coins.
healthValue = player.maxHealth / 3

# This function spawns a random item/unit in a random place.
def spawnRandomPlaced(type):
    x = game.randomInteger(12, 68)
    y = game.randomInteger(12, 56)
    game.spawnXY(type, x, y)

# Auxiliary variables, goals and UI.
itemInterval = 2
itemSpawnTime = 0
game.collected = 0
ui.track(game, "time")
ui.track(game, "collected")
ui.track(player, "health")
game.addCollectGoal(10)
game.addSurviveGoal()

# Let's make ogres aggressive.
def onSpawn(event):
    unit = event.target
    unit.behavior = "AttacksNearest"

game.setActionFor("munchkin", "spawn", onSpawn)

# It defines the result of collected items.
def onCollect(event):
    # event.target contains the collector.
    collector = event.target
    # event.other contains the collected item.
    item = event.other
    # Increase the game.collected by 1.
    game.collected +=1
    # If item's type is "gold-coin":
    if item.type=="gold-coin":
        # Increase collector.health by healthValue:
        collector.health+=healthValue
    # If item's type is "gem":
    if item.type=="gem":
        # Reduce  the collector's health by healthValue:
        collector.health-=healthValue

# Assign onCollect handler for "player" on "collect" event.
player.on("collect", onCollect)

def checkSpawnTimer():
    if game.time >= itemSpawnTime:
        spawnRandomPlaced("gem")
        spawnRandomPlaced("gold-coin")
        spawnRandomPlaced("munchkin")
        itemSpawnTime += itemInterval

while True:
    checkSpawnTimer()
