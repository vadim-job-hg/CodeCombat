# https://codecombat.com/play/level/hit-and-freeze
# You are trapped, but still dangerous.
# Don't do any unnecessary movements, it'll be painful.
# Hit ogres only they are near you and you can reach them with your sword.

# This function check if the 'enemy' in your attack range.
# The function returns a boolean value: True or False
def inAttackRange(enemy):
    distance = hero.distanceTo(enemy)
    # Almost all swords have attack range equal 3.
    if distance <= 3:
        return True
    else:
        return False

while True:
    # Find the nearest enemy and store it in the variable.
    #enemy = hero.findNearestEnemy()
    enemy = hero.findNearestEnemy()
    # Call 'inAttackRange' function with the parameter from the previous step.
    # Save the result in a variable ('canAttack' for example).
    canAttack = inAttackRange(enemy)
    # If the result of the function is true, then attack the enemy.
    if canAttack:
        hero.attack(enemy)
    pass
