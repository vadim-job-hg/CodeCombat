hits = 0
while hits<10:
    enemy = self.findNearestEnemy()
    if(enemy):
        self.attack(enemy)
        hits += 1
# Как только закончишь, отступай к засаде.
if(enemy and self.isReady('cleave')):
    self.cleave(enemy)
self.moveXY(51, 31)
self.moveXY(68, 27)
self.moveXY(79, 33)
