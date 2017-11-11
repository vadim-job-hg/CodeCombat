# http://codecombat.com/play/level/yak-heist
# Senick needs big bait for a big burl!
# Help Senick find an above average yak!
# Don't pick one too deep in the herd, or risk angering the group.

# This function should return the average size of all the yaks:
def averageSize(yaks):
    sum = 0
    # Go through each yak and add its size to the sum.
    for yak in yaks:
        sum = sum + yak.size
    return sum / yaks.length


yaks = hero.findEnemies()
avgSize = averageSize(yaks)
bestYak = None
closestDist = 9999
for i in range(len(yaks)):
    yak = yaks[i]
    yakDistance = hero.distanceTo(yak)
    yakSize = yak.size
    # Check if the yak is:
    if yakDistance < closestDist and yakSize > avgSize:
        closestDist = yakDistance
        bestYak = yak
        # The distance is closer than the current 'closestDist' AND
        # The size is bigger than the 'avgSize'.

        # Update the 'bestYak' and 'closestDist'

# Say the 'bestYak':
hero.say(bestYak)
