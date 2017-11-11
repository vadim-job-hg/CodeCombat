# http://codecombat.com/play/level/tactical-strike
# Победи огров.
while True:
    hero.moveDown()
    hero.moveRight()
    enemy = hero.findNearestEnemy()
    while enemy:
        hero.attack(enemy)
        enemy = hero.findNearestEnemy()
    hero.moveDown()