while True:
    hero.moveXY(43, 50)
    topEnemy = hero.findNearestEnemy()
    if topEnemy:
        hero.buildXY("fire-trap", 43, 50)

    hero.moveXY(25, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.buildXY("fire-trap", 23, 34)

    hero.moveXY(42, 22)
    bottomEnemy = hero.findNearestEnemy()
    if bottomEnemy:
        hero.buildXY("fire-trap", 42, 22)
