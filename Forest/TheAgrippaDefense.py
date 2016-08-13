while True:
    enemy = self.findNearestEnemy()
    if (enemy):
        dist = self.distanceTo(enemy)
        if (dist < 5):
            if (self.isReady("cleave")):
                self.cleave(enemy)
            else:
                self.attack(enemy)
