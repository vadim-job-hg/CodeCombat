yak = hero.findNearestEnemy()
while yak:
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    yak = hero.findNearestEnemy()
hero.moveXY(38, 58)
