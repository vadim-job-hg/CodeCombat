if (1 + 1 + 1 == 3):
    hero.moveXY(15, 41)

if (2 + 2 == 5):
    hero.moveXY(25, 16)

if (2 + 2 == 4):
    hero.moveXY(25, 15)

if (1 + 1 < 3):
    enemy = hero.findNearestEnemy()
    if (enemy):
        hero.attack(enemy)

if (2 < 4):
    hero.moveXY(53, 18)

if (True):
    hero.moveXY(55, 25)

if (False):
    hero.moveXY(55, 25)
