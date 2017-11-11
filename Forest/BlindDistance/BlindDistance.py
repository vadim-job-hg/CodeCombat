# https://codecombat.com/play/level/blind-distance
# It's an ambush and your only weapon is the old, blind wizard.
# Your task is to tell him the distance to the coming ogres.
# Don't worry about the direction.
# The wizard's powers are limited, use them only when see an ogre.

# This function finds the nearest enemy and returns the distance to it.
# If there is not enemy, the function returns 0.
def nearestEnemyDistance():
    #enemy = hero.findNearestEnemy()
    enemy = hero.findNearestEnemy()
    result = 0
    if enemy:
        result = hero.distanceTo(enemy)
    return result

while True:
    # Call 'nearestEnemyDistance' function and save a result in a variable 'distance'.
    distance = nearestEnemyDistance()
    # If 'distance' is greater than 0:
    if distance>0:
        # Say the distance.
        hero.say(distance)
    pass
