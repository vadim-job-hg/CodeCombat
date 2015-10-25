attack = False
loop:    
    enemy = self.findNearestEnemy();
    if(enemy):
        dist = self.distanceTo(enemy);
    if(dist<10 and attack):    
        if(self.isReady("cleave")):
            self.cleave(enemy)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
        elif(dist<5):
             self.attack(enemy)  
        else:
            self.shield()             
    else:
        self.shield()
    if(dist<5):
        attack = True
    else:
        attack = False
