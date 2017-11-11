# https://codecombat.com/play/level/tomb-ghost
# The only exit is blocked by ogres.
# Hide from the skeletons and kill ogres one by one.

# This function should attack an enemy and hide.
def hitOrHide(target):
    # If 'target' exists:
    if target:
        hero.attack(target)
        # Attack 'target' and then move to the red mark.
    else:
        hero.moveXY(32, 17)
    pass

while True:
    enemy = hero.findNearestEnemy()
    hitOrHide(enemy)
