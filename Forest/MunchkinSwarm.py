while True:
    enemy = self.findNearestEnemy()
    dist = self.distanceTo(enemy)
    if (dist < 5):
        if self.isReady('cleave'):
            self.cleave(enemy)
        else:
            self.attack(enemy)
    else:
        self.attack("Chest")
