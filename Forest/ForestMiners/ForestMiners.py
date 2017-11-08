# https://codecombat.com/play/level/forest-miners
# Stuck in the ogre forest!
# Check both mining point for ogres and call peasants if it's safe.
# Don't call peasants when you kill an ogre because ogre guards will be there.

# This function should check the if there is 'target' or it's safe.
def checkEnemyOrSafe(target):
    # Write this function.
    # If 'target' exist, then attack it.
    # Otherwise say something to call peasants.
    if target:
        hero.attack(target)
    else:
        hero.say('yahoo')
    pass


# Move and check the marks: the top right first, then the bottom left one.
while True:
    # Move and check the top right point.
    hero.moveXY(64, 54);
    enemy = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy)

    # Move and check the bottom left point.
    hero.moveXY(16, 14);
    enemy = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy)

