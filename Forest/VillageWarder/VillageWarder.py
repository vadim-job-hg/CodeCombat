# https://codecombat.com/play/level/village-warder
# This function attacks the nearest enemy.
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

def findAndCleaveEnemy():
    # Define a function to cleave enemies (but only when the ability is ready).
    enemy = hero.findNearestEnemy()
    if enemy and hero.isReady('cleave'):
        hero.cleave(enemy)
    pass

# In your main loop, patrol, cleave, and attack.
while True:
    # Move to the patrol point, cleave, and attack.
    hero.moveXY(35, 34)
    findAndCleaveEnemy()
    findAndAttackEnemy()
    hero.moveXY(60, 31)
    # Move to the other point, cleave, and attack.
    findAndCleaveEnemy()
    findAndAttackEnemy()
