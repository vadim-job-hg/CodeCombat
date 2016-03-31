#http://codecombat.com/play/level/the-agrippa-defense-b
def enemyInRange(enemy):
    # Return true if the enemy is less than 5 units away.
    if self.distanceTo(enemy)<5:
        return True
    return False

def cleaveOrAttack(enemy):
    if self.isReady('cleave'):
        self.cleave(enemy)
    else:
        self.attack(enemy)

while True:
    enemy = self.findNearestEnemy()
    if enemy:
        # Check the distance of the enemy by calling enemyInRange.
        if enemyInRange(enemy):
            cleaveOrAttack(enemy)

