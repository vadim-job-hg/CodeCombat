# https://codecombat.com/play/level/forest-garden

# Grow the perfect rectangular flower fence.

# Use the certain sizes for the flower rectangular.
gardener = hero.findNearest(hero.findFriends())
gardenWidth = gardener.gardenWidth
gardenHeight = gardener.gardenHeight
# Start grow from the initial position.
hero.toggleFlowers(True)
x = hero.pos.x
y = hero.pos.y
# Move to all corners one by one and return to the start.
hero.moveXY(x+gardenWidth, y)
hero.moveXY(x+gardenWidth, y-gardenHeight)
hero.moveXY(x, y-gardenHeight)
hero.moveXY(x, y)
