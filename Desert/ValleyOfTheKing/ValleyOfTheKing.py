# Attack the skeleton while its health is more than a third of its maxHealth.
# Then run away from it.
enemy = hero.findNearestEnemy()
hero.debug('debug', enemy.health, enemy.maxHealth)
while enemy.health>enemy.maxHealth/3:
    hero.attack(enemy)
hero.moveXY(39, 22)
