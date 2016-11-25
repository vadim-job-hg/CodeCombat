while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if (flag):
        hero.pickUpFlag(flag)
    elif (enemy):
        dist = hero.distanceTo(enemy)
        if (dist < 5):
            if (hero.isReady("cleave")):
                hero.cleave(enemy)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            else:
                hero.attack(enemy)
