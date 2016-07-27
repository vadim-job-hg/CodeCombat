# http://codecombat.com/play/level/village-rover
# This defines a function called findAndAttackEnemy
def findAndAttackEnemy():
    enemy = self.findNearestEnemy()
    if enemy and self.distanceTo(enemy) < 20:
        self.attack(enemy)


# This code is not part of the function.
while True:
    # Now you can patrol the village using findAndAttackEnemy
    self.moveXY(35, 34)
    findAndAttackEnemy()

    # Now move to the right entrance.
    self.moveXY(60, 31)
    findAndAttackEnemy()
    # Use findAndAttackEnemy
