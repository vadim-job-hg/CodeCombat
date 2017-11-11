# https://codecombat.com/play/level/grid-minefield
# The ogre formation is marching at the village.
# We have 90 seconds to build a minefield.
# We'll use their strict formation against them.

# Use nested loops to build the grid minefield.
# First iterate x coordinates from 12 to 60 with step 8.
for x in range(12, 12 + 8 * 6, 8):
    # For each x iterate y cordinates from 12 to 68 with step 8.
    for y in range(12, 12 + 8 * 7, 8):
        # For each point build "fire-trap" there.
        hero.buildXY("fire-trap", x, y)
        pass
    # After each column, it's better to move right to avoid own traps.
    hero.moveXY(hero.pos.x + 8, hero.pos.y)

# Now wait and watch the coming ogres.
# When they are near (about 20 metres from the hero) blow mines with your hero.
# Just move at the nearest mine when it's the time.
while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) <= 20:
        hero.moveXY(x, y)
