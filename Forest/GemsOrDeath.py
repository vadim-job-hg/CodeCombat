if (1 + 1 + 1 == 3):
    self.moveXY(15, 41)

if (2 + 2 == 5):
    self.moveXY(25, 16)

if (2 + 2 == 4):
    self.moveXY(25, 15)

if (1 + 1 < 3):
    enemy = self.findNearestEnemy()
    if (enemy):
        self.attack(enemy)

if (2 < 4):
    self.moveXY(53, 18)

if (True):
    self.moveXY(55, 25)

if (False):
    self.moveXY(55, 25)
