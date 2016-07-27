# http://codecombat.com/play/level/crux-of-the-desert
# Ogres are assaulting the Crux of the Desert!
# Defend against the waves by checking which direction the ogres are coming.
# Store the results of comparisons as variables to make your code easy to read.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # An enemy is to the left if the hero's x is greater than the enemy's.
        isLeft = hero.pos.x > enemy.pos.x
        # An enemy is above if the enemy's y is greater than the hero's.
        isAbove = hero.pos.y < enemy.pos.y
        isUnder = hero.pos.y > enemy.pos.y
        # Check if the enemy is to the right of the hero:
        isRight = hero.pos.x < enemy.pos.x
        #  If an enemy is above and to the left, build a fire-trap accordingly.

        # If an enemy is above and to the left, build a fire-trap accordingly.
        if isLeft and isAbove:
            hero.buildXY("fire-trap", 40 - 20, 34 + 17)
        # Check if an enemy is above and to the right:
        elif isRight and isAbove:
            hero.buildXY("fire-trap", 40 + 20, 34 + 17)
        # Check if an enemy is below and to the left:
        elif isLeft and isUnder:
            hero.buildXY("fire-trap", 40 - 20, 34 - 17)
        # Check if an enemy is below and to the right:
        elif isRight and isUnder:
            hero.buildXY("fire-trap", 40 + 20, 34 - 17)
        hero.moveXY(40, 34)
    else:
        hero.moveXY(40, 34)
