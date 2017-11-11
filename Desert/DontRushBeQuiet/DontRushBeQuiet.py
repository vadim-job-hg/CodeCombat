# http://codecombat.com/play/level/dont-rush-be-quiet
# Dodge the cannons and collect 8 gems.
# Watch out, cannons are ready to fire!
# Move slow along a special pattern to confuse them.

# This function returns a value from 0 to 30:
def mod30(n):
    if n >= 30:
        return n - 30
    else:
        return n


# This function should return a value from 0 to 40:
def mod40(n):
    # Use an if-statement to return the correct value.
    if n >= 40:
        return n - 30
    else:
        return n


# You don't need to change the following code:
while True:
    time = hero.now()
    x = mod30(time) + 25
    y = mod40(time) + 10
    item = hero.findNearestItem()
    if (item and hero.distanceTo(item) < 7):
        hero.moveXY(item.pos.x, item.pos.y)
        hero.moveXY(x, y)
    else:
        hero.moveXY(x, y)
