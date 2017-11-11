while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    if (flag):
        hero.pickUpFlag(flag)
    elif (enemy):
        dist = hero.distanceTo(enemy)
        if (hero.isReady("cleave") and dist < 5):
            hero.cleave(enemy)
        else:
            if (hero.isReady("bash") and dist < 5):
                hero.bash(enemy);
            elif (dist < 5):
                hero.attack(enemy)
            else:
                hero.shield()
