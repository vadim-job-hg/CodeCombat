# https://codecombat.com/play/level/if-stravaganza
# Defeat the ogres from within their own camp!

while True:
    enemy = hero.findNearestEnemy()
    # Use an if-statement to check if an enemy exists:
    if enemy:
        # Attack the enemy if it exists:
        hero.attack(enemy)
