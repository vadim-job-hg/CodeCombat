# https://codecombat.com/play/level/woodland-cubbies
# Navigate through the woods, but be on the lookout!
# These forest cubbies may contain ogres!
hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# The if-statement will check if a variable has an ogre.
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(49, 51)
enemy2 = hero.findNearestEnemy()
if enemy2:
    # Attack the enemy2 here:
    hero.attack(enemy2)
    hero.attack(enemy2)
    pass

hero.moveXY(58, 14)
enemy3 = hero.findNearestEnemy()
# Use an if-statement to check if enemy3 exists:
if enemy3:
    # If enemy3 exists, attack it:
    hero.attack(enemy3)
    hero.attack(enemy3)

