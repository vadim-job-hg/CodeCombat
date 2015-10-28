loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    if(flag):
        self.pickUpFlag(flag) 
    elif (enemy):
       dist = self.distanceTo(enemy)        
       if(self.isReady("cleave") and dist <5):
            self.cleave(enemy)
        else:
            if(self.isReady("bash") and dist <5):
                self.bash(enemy);
            elif(dist <5 ):
                self.attack(enemy)
            else:
                self.shield()     