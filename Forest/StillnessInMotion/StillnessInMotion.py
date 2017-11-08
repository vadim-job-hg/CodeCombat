while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance and distance < 5:
            hero.attack(enemy)
        else:
            hero.shield()
    else:
        hero.moveXY(40, 34)
