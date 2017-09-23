# https://codecombat.com/play/level/rational-defense
# Protect the peasants.

# Move the peasants away from the woods.
def hideUnits(units):
    for i in range(len(units)):
        unit = units[i]
        hero.command(unit, "move", {'x': 34, 'y': 10 + i * 12})

# All peasants know in what order to build traps.
peasants = hero.findFriends()
buildOrder = peasants[0].buildOrder
separator = ","
# Split buildOrder with comma (",")
# and save the result to the variable "types":
types = buildOrder.split(',')

# There are the same number of peasants as types.
for index in range(len(peasants)):
    peasant = peasants[index]
    x = 16
    y = 10 + index * 12
    # Get buildType by index from the array of types:
    buildType = types[index]
    # Command the peasant buildXY buildType at x and y:
    hero.command(peasant, 'buildXY', buildType, x, y)

# Watch for enemies and move peasants when ogres attack.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hideUnits(peasants)
        break

# Fight the ogres:
# Defend the last point yourself:
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
