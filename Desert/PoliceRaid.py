# https://codecombat.com/play/level/police-raid
# Wait for ogres, defeat them and collect gold.

while True:
    enemies = hero.findEnemies()
    # That variable is used to iterate "enemies" array.
    enemyIndex = 0
    # While it less than the array length:
    while enemyIndex < len(enemies):
        # Get an enemy from the array.
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        # Increase "enemyIndex" by one.
        enemyIndex += 1
    coins = hero.findItems()
    # That variable is used to iterate "coins" array.
    coinIndex = 0
    while coinIndex < len(coins):
        # Get a coin from the "coins" array at coinIndex.
        coin = coins[coinIndex]
        # Collect that coin.
        hero.moveXY(coin.pos.x, coin.pos.y)
        # Increase "coinIndex" by one.
        coinIndex = coinIndex + 1
        pass
