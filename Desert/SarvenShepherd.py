while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.type != "sand-yak" and enemy.health > 0:
            hero.attack(enemy)
        enemyIndex += 1
