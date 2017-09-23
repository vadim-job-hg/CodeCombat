while True:
    item = hero.findNearestItem()
    if (item):
        if (hero.isReady("jump")):
            hero.jumpTo({'x': item.pos.x, 'y': item.pos.y})
        else:
            hero.move(item.pos)
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    enemy = hero.findNearestEnemy()
    if enemy:
        soldiers = hero.findFriends()
        soldierIndex = 0
        while (soldierIndex < len(soldiers)):
            soldier = soldiers[soldierIndex]
            hero.command(soldier, "attack", enemy)
            soldierIndex += 1
