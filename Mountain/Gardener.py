# https://codecombat.com/play/level/gardener
# We need square flower fence around statues.

# This function make a square around {cx, cy} point.
def growSquare(cx, cy, side):
    # Move to any corners of the square.
    width = side/2
    hero.moveXY(cx-width, cy-width)
    # Start growing.
    hero.toggleFlowers(True)
    # Now move to all other corners one by one.
    # Use clockwise or countercloclwise order.
    hero.moveXY(cx-width, cy+width)
    hero.moveXY(cx+width, cy+width)
    hero.moveXY(cx+width, cy-width)
    # Don't forget to return in the first corner.
    hero.moveXY(cx-width, cy-width)
    #hero.moveXY(cx, cy)
    # Stop growing.
    hero.toggleFlowers(False)

# The keeper will say where to grow flowers.
keeper = hero.findNearest(hero.findFriends())
points = keeper.pointsForWork
# All squares should have the same size.
squareSize = 8
# We don't need excess flowers.
hero.toggleFlowers(False)

for pos in points:
    # Don't forget complete this function.
    growSquare(pos.x, pos.y, squareSize)
