while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if item is not None:
        hero.moveXY(item.pos.x, item.pos.y)
    if enemy is not None:
        dist = hero.distanceTo(enemy)
        if (enemy.type == 'thrower'):
            hero.attack(enemy)
            hero.attack(enemy)
        elif (hero.isReady("power-up") and (enemy.type == "burl" or enemy.type == "ogre")):
            hero.powerUp()
        else:
            if (dist < 15):
                if (hero.isReady("cleave") and dist < 15):
                    hero.cleave(enemy)
                elif (hero.isReady("bash") and dist < 15):
                    hero.bash(enemy)
                elif (hero.isReady("power-up")):
                    hero.powerUp()
                elif (dist > 10):
                    hero.attack(enemy)
                    hero.attack(enemy)
                else:
                    hero.shield()
            else:
                hero.shield()
