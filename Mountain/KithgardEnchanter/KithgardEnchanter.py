# http://codecombat.com/play/level/kithgard-enchanter
# This level is on mountain. I don't know why!


# Define your own simple movement functions.
# Define moveRight
# Note: each function should move the hero 12 meters!
def moveRight():
    target = {"x": hero.pos.x + 12, "y": hero.pos.y}
    while hero.distanceTo(target) > 0:
        hero.move(target);


# Define moveLeft
def moveLeft():
    target = {"x": hero.pos.x - 12, "y": hero.pos.y}
    while hero.distanceTo(target) > 0:
        hero.move(target);


# Define moveUp
def moveUp():
    target = {"x": hero.pos.x, "y": hero.pos.y + 12}
    while hero.distanceTo(target) > 0:
        hero.move(target);


# Define moveDown
def moveDown():
    target = {"x": hero.pos.x, "y": hero.pos.y - 12}
    while hero.distanceTo(target) > 0:
        hero.move(target);


# Now, use those functions!
moveRight()
moveDown()
moveUp()
moveUp()
moveRight()
