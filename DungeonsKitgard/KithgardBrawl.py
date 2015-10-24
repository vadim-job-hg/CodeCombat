loop:
    enemy = self.findNearestEnemy()
    item  = self.findNearestItem()
    if item is not None:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy is not None:
        if self.isReady("power-up"):
            self.powerUp()
        elif self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy) 
        
