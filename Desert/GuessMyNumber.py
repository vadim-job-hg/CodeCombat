# http://codecombat.com/play/level/guess-my-number
# You need to guess the number from 0 to 1000 (0 <= n <= 1000).
# You have 10 attempts!
# For each attempt Riddler will say if the number is less or greater.
# If the guessed number is less than your try, then a munchkin ogre appears.
# Else a scout ogre appears.
def number():
    return Math.round((topEnd - lowEnd) / 2) + lowEnd
    # return Math.round(Math.random()*(topEnd-lowEnd)) + lowEnd


lowEnd = 0
topEnd = 1000
curnumber = 500
while True:
    # You need to kill the enemy before the next attempt.
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == 'scout':
            lowEnd = curnumber + 1
        else:
            topEnd = curnumber - 1
        # "scout" is 'greater', "munchkin" is less.
        # Prepare for the next attempt and wipe out the ogre.

        hero.attack(enemy)
    else:
        # Make your next attempt and say it.
        curnumber = number()
        hero.say(curnumber)
