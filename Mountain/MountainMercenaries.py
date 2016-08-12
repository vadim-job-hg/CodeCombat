# Соберите монеты, чтобы вызвать солдат и атаковать ими врагов.

while True:  # Переход к ближайшей монете.
    # Используйте 'move' вместо 'moveXY', чтобы командовать постоянно.
    item = self.findNearest(self.findItems())
    if (item):
        self.move(item.pos)
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")
    enemy = self.findNearest(self.findEnemies())
    if enemy:
        soldiers = self.findFriends()
        soldierIndex = 0
        while (soldierIndex < len(soldiers)):
            soldier = soldiers[soldierIndex]
            self.command(soldier, "attack", enemy)
            soldierIndex += 1
