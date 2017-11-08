# https://codecombat.com/play/level/mail-interceptor
# Intercept all ogre messengers from ambush. 

def ambushAttack(target):
    #  Attack the target if it exists and return to the mark.
    # Write the function:
    if(target and target.pos.x>38):
        hero.attack(target)
    else:
        hero.moveXY(52,36)
    pass

while True:
    ogre = hero.findNearestEnemy()
    ambushAttack(ogre)

