# Соберите монеты, чтобы вызвать солдат и атаковать ими врагов.

while True:  # Переход к ближайшей монете.
    # Используйте 'move' вместо 'moveXY', чтобы командовать постоянно.
    item = hero.findNearest(hero.findItems())
    if (item):
        hero.move(item.pos)
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        soldiers = hero.findFriends()
        soldierIndex = 0
        while (soldierIndex < len(soldiers)):
            soldier = soldiers[soldierIndex]
            hero.command(soldier, "attack", enemy)
            soldierIndex += 1
