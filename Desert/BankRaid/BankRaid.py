while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        enemyIndex += 1
    coins = hero.findItems()
    coinIndex = 0
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        hero.moveXY(coin.pos.x, coin.pos.y)
        coinIndex = coinIndex + 1
