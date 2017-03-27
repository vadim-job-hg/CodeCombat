# https://codecombat.com/play/level/short-sighted-burl
# The gold is guarded by a burl.
# The burl is short-sighted but it has good hearing.
# Collect coins and run unless the burl will find you.

# Write the function "checkTakeRun".
# It should take one parameter -- an item.
# If the item exists, take it.
# Move to the start point (the green mark) whether the item or no.
def checkTakeRun(item):
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    hero.moveXY(40, 12)

# Don't change this code. Just write the function.
while True:
    hero.moveXY(16, 56)
    item = hero.findNearestItem()
    checkTakeRun(item)
    hero.moveXY(64, 56)
    item = hero.findNearestItem()
    checkTakeRun(item)
