loop:
    enemys = self.findEnemies()
    items = self.findItems()
    item = self.findNearest(items)
    enemy = self.findNearest(enemys)
    if(enemy and self.distanceTo(enemy)<15):
        self.attack(enemy)
    elif(item):
        if(self.isReady('jump')):
            self.jumpTo(item.pos)
        else:
            self.move(item.pos)

