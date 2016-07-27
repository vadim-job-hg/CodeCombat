loop:
flag = self.findFlag()
enemy = self.findNearestEnemy()
if (flag):
    self.pickUpFlag(flag)
elif (enemy):
    dist = self.distanceTo(enemy)
    if (dist < 5):
        if (self.isReady("cleave")):
            self.cleave(enemy)
        elif (self.isReady("bash")):
            self.bash(enemy)
        else:
            self.attack(enemy)
