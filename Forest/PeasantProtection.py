loop:
    enemy = self.findNearestEnemy();
    distance = self.distanceTo(enemy);
    if (distance < 10):
        self.attack(enemy)  
    else:    
        self.moveXY(39, 37)
