while True:
    enemy = hero.findNearestEnemy()
    if (enemy):
        dist = hero.distanceTo(enemy)
        if (dist < 5):
            if (hero.isReady("cleave")):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)
