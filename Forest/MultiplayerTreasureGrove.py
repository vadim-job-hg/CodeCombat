while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    dist_item = 9999999
    dist_enemy = 99999999
    if item:
        dist_item = hero.distanceTo(item)
    if enemy:
        dist_enemy = hero.distanceTo(enemy)
    if ((dist_enemy < 10) or (dist_item > dist_enemy)):
        if (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
        else:
            hero.shield()
            hero.attack(enemy)
    elif (item):
        hero.moveXY(item.pos.x, item.pos.y)
    else:
        hero.moveXY(42, 30)
