def checkAndAttack(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        while enemy.health>0:
            hero.attack(enemy)

checkAndAttack(24, 42)
checkAndAttack(27, 60)
checkAndAttack(43, 51)
checkAndAttack(39, 25)
checkAndAttack(55, 29)
