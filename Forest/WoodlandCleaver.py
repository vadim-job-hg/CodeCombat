self.moveXY(23, 23);
loop:
enemy = self.findNearestEnemy()
if (self.isReady("cleave")):
    self.cleave(enemy)
else:
    self.attack(enemy)
