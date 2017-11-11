# https://codecombat.com/play/level/weakest-quickest

# Defeat shamans to survive.

# The function find the weakest enemy.
def findWeakestEnemy():
    enemies = hero.findEnemies()
    weakest = None
    leastHealth = 99999
    enemyIndex = 0
    # Loop through enemies:
    for enemy in enemies:
        # If an enemy's health is less than leastHealth:
        if enemy.health<leastHealth:
            # Make it the weakest
            weakest = enemy
            # and set leastHealth to its health.
            leastHealth = enemy.health
    return weakest

while True:
    # Find the weakest enemy with the function:
    enemy = findWeakestEnemy()
    # If the weakest enemy here:
    if enemy:
        # Attack it!
        hero.attack(enemy)
    pass
