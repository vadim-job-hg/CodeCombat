loop:
    enemy = self.findNearestEnemy()
    if enemy is not None:
        if self.isReady("power-up"):
            self.powerUp()
        elif self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy) 
        
