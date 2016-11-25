# http://codecombat.com/play/level/village-rover
# This defines a function called findAndAttackEnemy
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 20:
        hero.attack(enemy)


# This code is not part of the function.
while True:
    # Now you can patrol the village using findAndAttackEnemy
    hero.moveXY(35, 34)
    findAndAttackEnemy()

    # Now move to the right entrance.
    hero.moveXY(60, 31)
    findAndAttackEnemy()
    # Use findAndAttackEnemy
