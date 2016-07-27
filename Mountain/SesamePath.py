# http://codecombat.com/play/level/sesame-path
# Say "Open Sesame" and a door will open.
# Only doors near you will hear you.
# There is only one route without forks.
# The distance between each point is 24m.
sesame = "Open Sesame"
distance = 24
previous = ""
while True:
    up = {'x': self.pos.x, 'y': self.pos.y + distance}
    down = {'x': self.pos.x, 'y': self.pos.y - distance}
    right = {'x': self.pos.x + distance, 'y': self.pos.y}
    left = {'x': self.pos.x - distance, 'y': self.pos.y}
    self.say(sesame)
    # Check each direction to see if the path is clear.
    # Be sure to check and record your previous direction!
    # Up
    if (self.isPathClear(self.pos, up) and previous != 'd'):
        self.moveXY(up.x, up.y)
        previous = 'u'
    # Right
    elif (self.isPathClear(self.pos, right) and previous != 'l'):
        self.moveXY(right.x, right.y)
        previous = 'r'
    # Down
    elif (self.isPathClear(self.pos, down) and previous != 'u'):
        self.moveXY(down.x, down.y)
        previous = 'd'
    # Left
    elif (self.isPathClear(self.pos, left) and previous != 'r'):
        self.moveXY(left.x, left.y)
        previous = 'l'
