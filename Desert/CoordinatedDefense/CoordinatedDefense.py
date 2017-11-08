# https://codecombat.com/play/level/coordinated-defense
# Protect peasants from ogres.

while True:
    # Get an array of enemies.
    enemies = hero.findEnemies()
    # If the array is not empty.
    if len(enemies) > 0:
        # Attack the first enemy from "enemies" array.
        hero.attack(enemies[0])
        # Return to the start position.
        hero.moveXY(40, 20)
        pass
