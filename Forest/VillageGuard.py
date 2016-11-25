# Patrol the village entrances.
# If you find an enemy, attack it.
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    # Now move to the right entrance.
    # Find the rightEnemy.
    # Use "if" to attack if there is a rightEnemy.
    hero.moveXY(60, 31)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
