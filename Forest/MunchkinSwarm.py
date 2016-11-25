while True:
    enemy = hero.findNearestEnemy()
    dist = hero.distanceTo(enemy)
    if (dist < 5):
        if hero.isReady('cleave'):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    else:
        hero.attack("Chest")
