middleX = 40
middleY = 35
loop:
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if(enemy):
        dist = self.distanceTo(enemy);
    if (enemy):
        if(self.isReady("cleave")):
            self.cleave(enemy)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
        else:
            self.attack(enemy)
    elif(item):
        moveToX = item.pos.x
        moveToY = item.pos.y
        self.moveXY(moveToX, moveToY)
    elif(True):
        self.moveXY(middleX, middleY)
