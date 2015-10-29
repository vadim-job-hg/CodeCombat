loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if (flag):
        self.pickUpFlag(flag)
    elif(enemy):
        dist = self.distanceTo(enemy)
        if(dist<25):
            if(self.isReady("cleave") and dist<5):
                self.cleave(enemy)
            else:
                if(self.isReady("bash")):
                    self.bash(enemy)
                else:
                    self.attack(enemy)
    else:
        self.shield()

