self.moveXY(23, 23);
while True:
    enemy = self.findNearestEnemy()
    if (self.isReady("cleave")):
        self.cleave(enemy)
    else:
        self.attack(enemy)
