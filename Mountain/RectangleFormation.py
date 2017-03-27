# https://codecombat.com/play/level/rectangle-formation
# Form up soldiers and archers in rectangle formations.

# The distance between units.
step = 8

# First form up soldiers.
sergeant = hero.findNearest(hero.findByType("soldier"))
# The coordinates of the bottom left corner.
soldierX = 8
soldierY = 8
# The width and height of the formation.
width = sergeant.rectWidth
height = sergeant.rectHeight

for x in range(soldierX, soldierX + width + 1, 8):
    for y in range(soldierY, soldierY + height + 1, 8):
        hero.summon("soldier")
        lastUnit = hero.built[len(hero.built)-1]
        # Command the last built unit move on the position.
        hero.command(lastUnit, "move", {'x':x, 'y':y })

# Next form up archers.
sniper = hero.findNearest(hero.findByType("archer"))
# The coordinates of the bottom left corner.
archerX1 = 48
archerY1 = 8
# The coordinates of the top right corner.
archerX2 = sniper.archerX2
archerY2 = sniper.archerY2

for x in range(archerX1, archerX2 + 1, 8):
    for y in range(archerY1, archerY2 + 1, 8):
        # Summon an archer.
        hero.summon("archer")
        # Find the last built unit.
        lastUnit = hero.built[len(hero.built)-1]
        # Command the last built unit move on the position.
        hero.command(lastUnit, "move", {'x':x, 'y':y })
