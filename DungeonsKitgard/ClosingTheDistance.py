while True:
    self.moveRight()
    enemy = self.findNearestEnemy()
    if (enemy):
        self.attack(enemy)
        self.attack(enemy)
