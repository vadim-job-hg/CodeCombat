hero.moveXY(23, 23);
while True:
    enemy = hero.findNearestEnemy()
    if (hero.isReady("cleave")):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
