loop:
    item = self.findNearest(self.findItems())
    if(item):
        if(self.isReady("jump")):
            self.jumpTo({'x':item.pos.x, 'y':item.pos.y})
        else:
            self.move(item.pos)
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")
    enemy = self.findNearest(self.findEnemies())
    if enemy:
        soldiers = self.findFriends()
        soldierIndex = 0
        while(soldierIndex<len(soldiers)):
            soldier = soldiers[soldierIndex]
            self.command(soldier, "attack", enemy)
            soldierIndex +=1
