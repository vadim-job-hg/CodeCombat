loop:
    enemy = self.findNearestEnemy()
    item  = self.findNearestItem()
    if item is not None:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy is not None:
        dist = this.distanceTo(enemy)
        if(enemy.type == 'thrower'):
            this.attack(enemy)   
        elif(this.isReady("power-up") and (enemy.type == "burl" or enemy.type == "ogre")):
            self.powerUp()
        else:
            if(dist<15):            
                 if(self.isReady("cleave") and dist<5):
                    self.cleave(enemy)
                 elif(this.isReady("bash") and dist<5):
                    self.bash(enemy)
                 elif(this.isReady("power-up")):
                    self.powerUp()
                 elif(dist<5):
                    self.attack(enemy)      
            else:
                 self.shield()
