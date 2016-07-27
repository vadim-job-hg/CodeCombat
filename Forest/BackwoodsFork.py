# https://codecombat.com/play/level/backwoods-fork
# Incoming ogres!
# Use the checkAndAttack function to make your code easy to read.

# This function has a parameter.
# An parameter is a way of passing information into a function.
def checkAndAttack(target):
    # The 'target' parameter is just a variable!
    # It contains the argument when the function was called.
    if target:
        hero.attack(target)
    hero.moveXY(43, 34)


while True:
    hero.moveXY(58, 52)
    topEnemy = hero.findNearestEnemy()
    checkAndAttack(topEnemy)
    hero.moveXY(58, 16)
    topEnemy = hero.findNearestEnemy()
    checkAndAttack(topEnemy)
    # Move to the bottom X mark.

    # Create a variable named bottomEnemy and find the nearest enemy.

    # Use the checkAndAttack function, and include the bottomEnemy variable.
