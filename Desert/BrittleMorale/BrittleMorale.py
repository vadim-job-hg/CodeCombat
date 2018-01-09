def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.health > strongestHealth:
            strongestHealth = enemy.health
            strongest = enemy
    return strongest


enemies = hero.findEnemies()
if enemies:
    hero.say(findStrongestEnemy(enemies))
