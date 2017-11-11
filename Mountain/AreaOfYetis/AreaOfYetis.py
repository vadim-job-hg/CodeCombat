# https://codecombat.com/play/level/area-of-yetis
# Defeat Yetis.

# The chosen one can stun yetis with the Shout.
chosen = hero.findFriends()[0]

# The power of the Shout is equal to the area of a circle.
radius = chosen.distanceTo(chosen.findNearestEnemy())
# The area of a circle can be calculated with the formula:
area = radius * radius * Math.PI
# Tell the area to the chosen one.
hero.say(area)
# Don't give up! Fight!
while True:
    enemyattack = hero.findNearestEnemy()
    if (enemyattack):
        hero.attack(enemyattack)

