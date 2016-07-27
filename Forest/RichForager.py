loop:
flag = self.findFlag()
enemy = self.findNearestEnemy()
item = self.findNearestItem()
if (flag):
    self.pickUpFlag(flag)
elif (enemy):
    dist = self.distanceTo(enemy)
    if (dist < 20):
        if (self.isReady("cleave")):
            self.cleave(enemy)
        elif (self.isReady("bash")):
            self.bash(enemy)
        else:
            self.attack(enemy)
elif (item):
    disti = self.distanceTo(item);
    if (disti < 15):
        self.moveXY(item.pos.x, item.pos.y)
