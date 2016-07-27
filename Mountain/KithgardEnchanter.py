# http://codecombat.com/play/level/kithgard-enchanter
# This level is on mountain. I don't know why!


# Define your own simple movement functions.
# Define moveRight
# Note: each function should move the hero 12 meters!
def moveRight():
    target = {"x": self.pos.x + 12, "y": self.pos.y}
    while self.distanceTo(target) > 0:
        self.move(target);


# Define moveLeft
def moveLeft():
    target = {"x": self.pos.x - 12, "y": self.pos.y}
    while self.distanceTo(target) > 0:
        self.move(target);


# Define moveUp
def moveUp():
    target = {"x": self.pos.x, "y": self.pos.y + 12}
    while self.distanceTo(target) > 0:
        self.move(target);


# Define moveDown
def moveDown():
    target = {"x": self.pos.x, "y": self.pos.y - 12}
    while self.distanceTo(target) > 0:
        self.move(target);


# Now, use those functions!
moveRight()
moveDown()
moveUp()
moveUp()
moveRight()
