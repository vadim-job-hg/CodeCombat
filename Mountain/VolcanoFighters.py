# https://codecombat.com/play/level/volcano-fighters
# Complete the paladin rectangle to protect people.

# The function find the most left unit.
def findMostLeft (units):
    if len(units) == 0:
        return None
    mostLeft = units[0]
    for unit in units:
        if unit.pos.x < mostLeft.pos.x:
            mostLeft = unit
    return mostLeft

# The function find the most bottom unit.
def findMostBottom (units):
    if len(units) == 0:
        return None
    mostBottom = units[0]
    for unit in units:
        if unit.pos.y < mostBottom.pos.y:
            mostBottom = unit
    return mostBottom

paladins = hero.findByType("paladin")
# Find the top left paladin with findMostLeft function.
ml = findMostLeft(paladins)
# Find the bottom right paladin with findMostBottom function
mb = findMostBottom(paladins)

# Use X coordinate from the top left paladin
# and Y coordinate from the bottom right paladin.
x = ml.pos.x
y = mb.pos.y
# Move to {X, Y} point from the previous step.
hero.moveXY(x, y)
# Shield while the volcano is erupting.
while True:
    hero.shield()

