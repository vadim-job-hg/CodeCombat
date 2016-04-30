#http://codecombat.com/play/level/tactical-strike
# Уничтожьте огров.
loop:
    hero.moveDown()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveUp(2)
    hero.moveRight(3)
    hero.moveDown(2)
    hero.moveLeft()
    hero.moveDown()
