loop:
    array = [[76, 52],[4, 50],[77, 20],[5, 20]]
    enemys = self.findEnemies()
    items = self.findItems()
    item = self.findNearest(items)
    enemy = self.findNearest(enemys)
    if(enemy and self.distanceTo(enemy)<20):
        if(self.pos.y>35):
            if(self.pos.x>40):
                self.moveXY(76, 52)
            else:
                self.moveXY(4, 50)
        else:
            if(self.pos.x>40):
                self.moveXY(77, 20)
            else:
                self.moveXY(5, 20)     
    elif(item):
        if(self.isReady('jump')):
            self.jumpTo(item.pos)
        else:
            self.moveXY(item.pos.x, item.pos.y)

