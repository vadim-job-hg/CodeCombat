def collectUntil(enoughGold):
    while enoughGold>hero.gold:
        item = hero.findNearestItem()
        hero.move(item.pos)
    pass

collectUntil(25)
hero.buildXY("decoy", 40, 52)
hero.moveXY(20, 52)
collectUntil(50)
hero.buildXY("decoy", 68, 22)
hero.buildXY("decoy", 30, 20)
