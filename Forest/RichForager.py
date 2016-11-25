while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if (flag):
        hero.pickUpFlag(flag)
    elif (enemy):
        dist = hero.distanceTo(enemy)
        if (dist < 20):
            if (hero.isReady("cleave")):
                hero.cleave(enemy)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            else:
                hero.attack(enemy)
    elif (item):
        disti = hero.distanceTo(item);
        if (disti < 15):
            hero.moveXY(item.pos.x, item.pos.y)
