hits = 0
while hits < 10:
    enemy = hero.findNearestEnemy()
    if (enemy):
        hero.attack(enemy)
        hits += 1
# Как только закончишь, отступай к засаде.
if (enemy and hero.isReady('cleave')):
    hero.cleave(enemy)
hero.moveXY(51, 31)
hero.moveXY(68, 27)
hero.moveXY(79, 33)
