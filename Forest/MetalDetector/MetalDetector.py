# https://codecombat.com/play/level/metal-detector
# The ogre camp is well guarded, but we'll use the ogres' greed.
# The artillery uses coins as a target.
# But the artillery rangefinder device isn't working in the forest.
# You'll be the rangefinder for the artillery.

# This function should find the nearest coin and return the distance to it.
# If there aren't coins, then the function should return 0 (zero).
def coinDistance():
    # Write the function.
    # item = hero.findNearestItem()
    item = hero.findNearestItem()
    if item:
        return hero.distanceTo(item)
    else:
        return 0
    pass


while True:
    distance = coinDistance()
    if distance > 0:
        hero.say(distance)

        pass
