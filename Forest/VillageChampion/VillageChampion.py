# https://codecombat.com/play/level/village-champion
# Incoming munchkins! Defend the town!

# Define your own function to fight the enemy!
# In the function, find an enemy, then cleave or attack it.
def attttaaaaacccckkkk():
    enemy =  hero.findNearestEnemy()
    #enemy = hero.findNearestEnemy()
    if enemy:
        if enemy and hero.isReady('cleave'):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)

# Move between patrol points and call the function.
while True:
    hero.moveXY(35, 34)
    # Use whatever function name you defined above.
    attttaaaaacccckkkk()
    hero.moveXY(47, 27)
    # Call the function again.
    attttaaaaacccckkkk()
    hero.moveXY(60, 31)
    # Call the function again.
    attttaaaaacccckkkk()
