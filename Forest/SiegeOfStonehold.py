while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if (flag):
        hero.pickUpFlag(flag)
    elif (enemy):
        dist = hero.distanceTo(enemy)
        if (dist < 25):
            if (hero.isReady("cleave") and dist < 5):
                hero.cleave(enemy)
            else:
                if (hero.isReady("bash")):
                    hero.bash(enemy)
                else:
                    hero.attack(enemy)
    else:
        hero.shield()
