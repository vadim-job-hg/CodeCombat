middleX = 61
middleY = 52
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    flag = hero.findFlag()
    if (enemy):
        dist = hero.distanceTo(enemy);
    if (enemy and dist < 10):
        if (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        else:
            hero.attack(enemy)
    elif (item):
        hero.move(item.pos)
    elif (True):
        hero.moveXY(middleX, middleY)
