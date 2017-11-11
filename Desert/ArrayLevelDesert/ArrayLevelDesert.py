# https://codecombat.com/play/level/array-level-desert

# The weakest health ogre does the most damage!
# Defeat the weakest health ogre first!

while True:
    enemies = hero.findEnemies()
    minHealth = 9999
    weakestOgre = None
    # Find the weakest ogre using a while loop.
    for enemy in enemies:
    # Attack the weakest ogre, if it exists.
        if enemy.health<minHealth:
            minHealth = enemy.health
            weakestOgre = enemy
    if weakestOgre:
        hero.attack(weakestOgre)
