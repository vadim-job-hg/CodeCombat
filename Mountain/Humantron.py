# https://codecombat.com/play/level/humantron

# Form the rectangle of units around the peasant.
# You need 2 archers and 2 soldiers.

# This function can be helpful.
def summonAndSend(type, x, y):
    hero.summon(type)
    unit = hero.built[len(hero.built)-1]
    hero.command(unit, "move", {"x": x, "y": y})

# The rectangle should be formed around the peasant.
centerUnit = hero.findNearest(hero.findFriends())
# It's the center of the rectangle.
center = centerUnit.pos
# Also you need the height and width.
rectWidth = centerUnit.rectWidth
rectHeight = centerUnit.rectHeight

# First soldier to the left bottom corner of the rectangle.
leftBottomX = center.x - rectWidth / 2
leftBottomY = center.y - rectHeight / 2
summonAndSend("soldier", leftBottomX, leftBottomY)

# An archer to the left top corner.
leftTopX = center.x - rectWidth / 2
leftTopY = center.y + rectHeight / 2
summonAndSend("archer", leftTopX, leftTopY)

# Summon and send a soldier to the right top corner.
rightTopX = center.x + rectWidth / 2
rightTopY = center.y + rectHeight / 2
summonAndSend("soldier", rightTopX, rightTopY)

# Summon and send an archer to the right bottom corner.
rightBottomX = center.x + rectWidth / 2
rightBottomY = center.y - rectHeight / 2
summonAndSend("archer", rightBottomX, rightBottomY)

# Now hide or fight.
hero.moveXY(68, 58)
