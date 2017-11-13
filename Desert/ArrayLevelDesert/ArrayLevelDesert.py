while True:
    enemies = hero.findEnemies()
    minHealth = 9999
    weakestOgre = None
    for enemy in enemies:
        if enemy.health<minHealth:
            minHealth = enemy.health
            weakestOgre = enemy
    if weakestOgre:
        hero.attack(weakestOgre)
