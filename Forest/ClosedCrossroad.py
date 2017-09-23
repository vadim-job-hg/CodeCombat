# https://codecombat.com/play/level/closed-crossroad
# That crossroad is busy and we should protect it.
# Use fire traps for the top and the bottom passages.
# Use fences for the left and the right passages.
# Don't always build, there are peasants using the crossroad.

# The function defines THREE parameters: a string and two numbers.
def maybeBuildSomething(buildType, x, y):
    # Use x and y as the coordinates to move to.
    hero.moveXY(x, y)
    # Check if there is an enemy nearby.
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 50:
        # If an enemy here, then build 'buildType' at the given 'x' and 'y'.
        hero.buildXY(buildType, x, y)


while True:
    # Calls maybeBuildSomething with "fire-trap" and the coordinates of the bottom passage.
    maybeBuildSomething("fire-trap", 40, 20)
    # Next use that function again, but with "fence" at the left entrance!
    maybeBuildSomething("fence", 26, 34)
    # Now use maybeBuildSomething with "fire-trap" at the top passage!
    maybeBuildSomething("fire-trap", 40, 50)
    # Now use maybeBuildSomething with "fence" at the right entry!
    maybeBuildSomething("fence", 54, 34)
