while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if (hero.isReady('bash')):
            hero.bash(enemy)
        else:
            hero.moveXY(40, 34)
    else:
        item = hero.findNearestItem()
        if item:
            hero.moveXY(item.pos.x, item.pos.y)
            hero.moveXY(40, 34)

# I found this works better.  With your method my hero could not bash far enough using 'Anya' 
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("bash"):
            hero.bash(enemy)
        else:
            hero.shield()
    else:
        gem = hero.findNearestItem()
        if gem:
            hero.moveXY(gem.pos.x, gem.pos.y)
        else:
            hero.moveXY(40, 34)
