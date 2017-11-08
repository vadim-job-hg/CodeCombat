# https://codecombat.com/play/level/canyon-of-storms
# A desert storm is coming!
# Yaks can detect when a storm is coming.

# This variable will be used as a condition.
yak = hero.findNearestEnemy()

# While there is a sand yak:
while yak:
    # Collect a coin.
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    # Update the variable "yak".
    yak = hero.findNearestEnemy()
# The yaks have hidden.
# Move to the hideout.
hero.moveXY(38, 58)
