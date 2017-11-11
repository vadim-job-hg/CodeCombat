while True:
    hero.moveRight()
    enemy = hero.findNearestEnemy()
    if (enemy):
        hero.attack(enemy)
        hero.attack(enemy)