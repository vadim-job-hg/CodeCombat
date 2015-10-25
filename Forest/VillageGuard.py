loop:
    self.moveXY(35, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.attack(leftEnemy)
        self.attack(leftEnemy)
    self.moveXY(60, 34)
    rightEnemy = self.findNearestEnemy()
    if rightEnemy:
        self.attack(rightEnemy)
        self.attack(rightEnemy)