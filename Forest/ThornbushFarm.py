loop:
self.moveXY(43, 50)
topEnemy = self.findNearestEnemy()
if topEnemy:
    self.buildXY("fire-trap", 43, 50)

self.moveXY(25, 34)
leftEnemy = self.findNearestEnemy()
if leftEnemy:
    self.buildXY("fire-trap", 23, 34)

self.moveXY(42, 22)
bottomEnemy = self.findNearestEnemy()
if bottomEnemy:
    self.buildXY("fire-trap", 42, 22)
