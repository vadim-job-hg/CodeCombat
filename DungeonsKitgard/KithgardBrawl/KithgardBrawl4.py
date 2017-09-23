while True:
    items = hero.findItems()
    item = hero.findNearest(items)
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    if (hero.health < hero.maxHealth / 3):
        item = hero.findNearestItem()
        if (item):
            if (hero.isReady("jump")):
                hero.jumpTo(item.pos)
            else:
                hero.move(item.pos)
    elif (enemy):
        if (hero.isReady("jump") and hero.distanceTo > 10):
            hero.jumpTo(enemy.pos)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        elif (hero.isReady("cleave")):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
