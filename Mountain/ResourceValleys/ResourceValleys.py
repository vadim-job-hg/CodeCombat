# http://codecombat.com/play/level/resource-valleys
# Collect all the coins!
# The peasants are unable to get the coins from other areas
# However, each area only spawns a certain value of coin!
# Filter through all the items and command the peasants accordingly.

def commandPeasant(peasant, coins):
    # Command the peasant to find the nearest of their coins array:
    item = peasant.findNearest(coins)
    if item:
        hero.command(peasant, "move", item.pos)


friends = hero.findFriends()
peasants = {
    "Aurum": friends[0],
    "Argentum": friends[1],
    "Cuprum": friends[2]
}

while True:
    items = hero.findItems()
    goldCoins = []
    silverCoins = []
    bronzeCoins = []
    for i in range(len(items)):
        item = items[i]
        if item.value == 3:
            goldCoins.push(item)
        # Put bronze and silver coins in their approriate array:
        elif item.value == 2:
            silverCoins.push(item)
        else:
            bronzeCoins.push(item)

    commandPeasant(peasants.Aurum, goldCoins)
    commandPeasant(peasants.Argentum, silverCoins)
    commandPeasant(peasants.Cuprum, bronzeCoins)
