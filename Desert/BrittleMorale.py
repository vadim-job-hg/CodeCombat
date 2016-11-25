# http://codecombat.com/play/level/brittle-morale
# Ogres are strong, but cowardly.
# Find and kill leader and they will retreat.
# You have only have one shot, but a deadly shot it will be.

# This function should return the enemy with the most health.
def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemyIndex = 0
    # Iterate over all the ogres to find the one with the most health.
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.health > strongestHealth:
            strongestHealth = enemy.health
            strongest = enemy
    return strongest


enemies = hero.findEnemies()
if enemies:
    hero.say(findStrongestEnemy(enemies))
