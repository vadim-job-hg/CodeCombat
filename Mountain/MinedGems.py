# https://codecombat.com/play/level/mined-gems

# Collect 4 gems. Don't touch gems from the inner circle.

# The radius of the gem-trap circle.
innerRadius = hero.distanceTo(hero.findNearestItem())

# This function check that a is definitely greater than b.
def definitelyGreater(a, b):
    return a > b + 0.5

centre = {"x": 40, "y": 34}
gems = hero.findItems()

# Iterate all gems:
for gem in gems:
    # If the distance to the current gems is definitely
    # greater than the inner radius:
    if definitelyGreater(hero.distanceTo(gem), innerRadius):
        # Collect the gem.
        hero.moveXY(gem.pos.x, gem.pos.y)
        # Return to the centre.
        hero.moveXY(centre.x, centre.y)

