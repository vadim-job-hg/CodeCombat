while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("bash"):
            hero.bash(enemy)
        else:
            hero.moveXY(40, 34)
            hero.shield()
    else:
        gem = hero.findNearestItem()
        if gem:
            hero.moveXY(gem.pos.x, gem.pos.y)
            hero.moveXY(40, 34)
        else:
            hero.moveXY(40, 34)
