middleX = 40
middleY = 35

loop:    
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if enemy:
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
        if((self.pos.x>middleX and item.pos.x<middleX) or (self.pos.x<middleX and item.pos.x>middleX)):
            moveToX = middleX
            moveToY = middleY 
        if((self.pos.y>middleY and item.pos.y<middleY) or (self.pos.y<middleY and item.pos.y>middleY)):
            moveToX = middleX
            moveToY = middleY 
        self.moveXY(moveToX, moveToY)
