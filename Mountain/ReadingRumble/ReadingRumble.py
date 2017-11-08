# https://codecombat.com/play/level/reading-rumble
# Defeat all incoming ogres.

while True:
    # Find the nearest enemy.
    enemy = hero.findNearestEnemy()
    # If there is an enemy, and it is a "brawler":
    if enemy and enemy.type == 'brawler':
        # Then say its name (.id) in UPPERCASE.
        hero.say(enemy.id.toUpperCase())
    # For other enemies, just fight.
    elif enemy:
        hero.attack(enemy)
    pass
