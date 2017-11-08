while True:
    enemy = hero.findNearestEnemy()
    if (hero.isReady("cleave")):
        hero.cleave(enemy)
    else:
        hero.shield()
