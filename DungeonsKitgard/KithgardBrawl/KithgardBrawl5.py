loop:
items = self.findItems()
item = self.findNearest(items)
enemies = self.findEnemies()
enemy = self.findNearest(enemies)
if (self.health < self.maxHealth / 3 * 2):
    item = self.findNearest(self.findItems())
    if (item):
        if (self.isReady("jump")):
            self.jumpTo(item.pos)
        else:
            self.move(item.pos)
elif (enemy):
    if (self.isReady("jump") and self.distanceTo > 10):
        self.jumpTo(enemy.pos)
    elif (self.isReady("bash")):
        self.bash(enemy)
    elif (self.isReady("power-up")):
        self.powerUp()
        self.attack(enemy)
    elif (self.isReady("cleave")):
        self.cleave(enemy)
    else:
        self.attack(enemy)
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
