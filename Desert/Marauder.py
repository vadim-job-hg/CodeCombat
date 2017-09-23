# https://codecombat.com/play/level/marauder
# Destroy mechs and collect gold from them.

while True:
    coin = hero.findNearest(hero.findItems())
    # While a coin exists:
    while coin:
        # Collect the coin.
        hero.moveXY(coin.pos.x, coin.pos.y)
        # Reassign the variable "coin" to the nearest item.
        coin = hero.findNearest(hero.findItems())
    enemy = hero.findNearestEnemy()
    if enemy:
        # While the enemy's health greater than 0.
        while enemy.health>0:
            # Attack it.
            hero.attack(enemy)
