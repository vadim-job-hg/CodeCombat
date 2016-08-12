while True:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if distance and distance < 5:
            self.attack(enemy)
        else:
            self.shield()
    else:
        self.moveXY(40, 34)
