# http://codecombat.com/play/level/sarven-treasure
while True:
    enemys = hero.findEnemies()
    items = hero.findItems()
    item = hero.findNearest(items)
    enemy = hero.findNearest(enemys)
    if (enemy and hero.distanceTo(enemy) < 15):
        hero.attack(enemy)
    elif (item):
        if (hero.isReady('jump')):
            hero.jumpTo(item.pos)
        else:
            hero.move(item.pos)
