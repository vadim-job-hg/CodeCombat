while True:
    enemy = self.findNearestEnemy()
    if (enemy):
        self.attack(enemy)
    else:
        self.moveXY(40, 34)
