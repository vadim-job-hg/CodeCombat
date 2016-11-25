middleX = 40
middleY = 35
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if (enemy):
        dist = hero.distanceTo(enemy);
    if (enemy):
        if (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
        else:
            hero.attack(enemy)
    elif (item):
        moveToX = item.pos.x
        moveToY = item.pos.y
        hero.moveXY(moveToX, moveToY)
    elif (True):
        hero.moveXY(middleX, middleY)
