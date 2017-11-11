while True:
    enemy = hero.findNearestEnemy();
    distance = hero.distanceTo(enemy);
    if (distance < 10):
        hero.attack(enemy)
    else:
        hero.moveXY(39, 37)
