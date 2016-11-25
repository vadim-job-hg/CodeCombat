# http://codecombat.com/play/level/operation-killdeer
# Lure the ogres into a trap.
# But, they are careful.
# These ogres will only follow the hero if the hero is injured.

# This function checks the hero's health and returns a Boolean value.
def shouldRun():
    if hero.health < hero.maxHealth / 2:
        return True
    else:
        return False


while True:
    # Run to the X only if the hero shouldRun().
    if (shouldRun()):
        hero.moveXY(75, 37)
        # Otherwise, fight!
