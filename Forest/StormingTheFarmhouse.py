# http://codecombat.com/play/level/storming-the-farmhouse
# Солдаты будут медленно прибывать, но огров будет больше.
# Простейшая loop атака не поможет выжить.
while True:
    flag = hero.findFlag()
    # target = hero.findNearestEnemy()
    target = hero.findNearest(hero.findEnemies())
    if flag:
        hero.pickUpFlag(flag)
    else:
        target = hero.findNearest(hero.findEnemies())
        if target:
            if (hero.isReady("cleave")):
                hero.cleave(target)
            else:
                hero.shield()
