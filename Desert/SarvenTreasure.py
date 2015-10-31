loop:
    enemys = self.findEnemies()
    items = self.findItems()
    item = self.findNearest(items)
    enemy = self.findNearest(enemys)
    if(enemy and self.distanceTo(enemy)<5):
        if(self.pos.y>35):
            if(self.pos.x>40):
                X = 76
                Y = 52
            else:
                X = 4
                Y = 50
        else:
            if(self.pos.x>40):
                X = 77
                Y = 20
            else:
                X = 5
                Y = 20  
        if(self.isReady('jump')):
            self.jumpTo({'x':X, 'y':Y})
        else:
            self.moveXY(X, Y)
    elif(item):
        if(self.isReady('jump')):
            self.jumpTo(item.pos)
        else:
            self.moveXY(item.pos.x, item.pos.y)

