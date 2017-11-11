# https://codecombat.com/play/level/explosive-works

# Put explosives to clear a dungeon passage.

# Mines should form a rectangle with the certain perimeter.
perimeter = 160
# The left bottom corner of the rectangle.
leftBottom = {"x": hero.pos.x, "y": hero.pos.y}

# One mine is placed already.
leftTop = hero.findHazards()[0].pos
# So we can find the height of the rectangle.
height = hero.distanceTo(leftTop)
# Find the width of the rectangle.
width = (perimeter - height*2)/2

# First, we need to place a mine in the left bottom corner.
hero.buildXY("fire-trap", leftBottom.x, leftBottom.y)
# Put a mine in the right bottom corner.
hero.buildXY("fire-trap", leftBottom.x+width, leftBottom.y)
# Put a mine in the right top corner.
hero.buildXY("fire-trap", leftBottom.x+width, leftTop.y)

# Now go to the demolitionist.
hero.moveXY(74, 32)
# Calculate the area of the rectangle to know the charge.
area = width*height
# Say the area of the rectangle to start the explosion.
hero.say(area)
