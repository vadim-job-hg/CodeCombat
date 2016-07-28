# https://codecombat.com/play/level/sleepwalkers
# Our sleepwalking peasants are returning.
# But sleeping yetis are also coming.
# DONT WAKE UP THEM!.
# We need to build fences to pass peasants and stop yetis.


# Senick's prepared the grid map how to build fences.
hunter = hero.findNearest(hero.findFriends())
fenceMap = hunter.getMap()


# This function convert grid map coordinates to x-y coordinates.
def convertCoor(row, col):
    return {'x': 34 + col * 4, 'y': 26 + row * 4}


# Iterate fenceMap and if an element equals 1, then build there a fence.
for ri, row in enumerate(fenceMap):
    for rx, col in enumerate(row):
        if (col == 1):
            coor = convertCoor(ri, rx)
            hero.buildXY('fence', coor.x, coor.y)

# Yetis wake up if they smell the hero near. Hide in the village.
hero.moveXY(22, 15)
