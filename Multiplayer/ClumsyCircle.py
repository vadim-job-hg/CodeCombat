# https://codecombat.com/play/level/clumsy-circle
# Find soldiers who breaks the circle.

# All soldiers should be on the circle with the radius:
circleRadius = 20

# The function checks if an unit is placed on the circle
# with the radius with the hero in the center.
def onCircle(unit, radius):
    distance = hero.distanceTo(unit)
    # We're using some inaccuracy.
    inaccuracy = 2
    minDistance = radius - inaccuracy
    maxDistance = radius + inaccuracy
    return distance <= maxDistance and distance >= minDistance

while True:
    soldiers = hero.findByType("soldier")
    for soldier in soldiers:
        # Use onCircle function to find
        # if the soldier not on the circle:
        if not(onCircle(soldier, circleRadius)):
            # Then say his/her name to get rid of that one.
            hero.say(soldier.id)
        pass
