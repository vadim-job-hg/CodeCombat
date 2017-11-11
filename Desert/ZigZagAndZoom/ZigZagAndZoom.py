# http://codecombat.com/play/level/zig-zag-and-zoom
# Escape from Death Valley!
# The archers firing at you are not your allies! Dodge the arrows!
# Move by with a zigzag pattern using real modulo functions.

# This function returns a value from 0 to 15:
def mod15(n):
    while n >= 15:
        n -= 15
    return n


# This function should return a value from 0 to 9:
def mod9(n):
    # Use a while loop to modify the parameter before returning
    while n >= 9:
        n -= 9
    return n


# Don't change the following code:
while True:
    time = hero.now()
    x = 10 + time
    if time < 30:
        y = 10 + 3 * mod15(time)
    elif time < 35:
        y = 20 + 3 * mod9(time)
    else:
        y = 34
        x = 71
    hero.moveXY(x, y)
