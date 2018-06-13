# Attack munchkins, call brawlers and ignore burls.

# This function defines the hero's behaviour about enemies.
def dealEnemy(enemy):
    # If enemy.type is "munchkin":
    if enemy.type=="munchkin":
        # Then attack it:
        hero.attack(enemy)
    # If the enemy's type is "brawler":
    if enemy.type=="brawler":
        # Then say something to call the brawler:
        hero.say('Get Over HEEERRREEE')
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)
