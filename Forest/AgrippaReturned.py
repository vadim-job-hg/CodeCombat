# https://codecombat.com/play/level/agrippa-returned
def enemyInRange(enemy):
    # Return true if the enemy is less than 5 units away.
    if hero.distanceTo(enemy)<5:
        return True
    return False

def cleaveOrAttack(enemy):
    if hero.isReady('cleave'):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Check the distance of the enemy by calling enemyInRange.
        if enemyInRange(enemy):
            cleaveOrAttack(enemy)
