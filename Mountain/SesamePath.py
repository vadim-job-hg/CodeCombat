# http://codecombat.com/play/level/sesame-path
# Say "Open Sesame" and a door will open.
# Only doors near you will hear you.
# There is only one route without forks.
# The distance between each point is 24m.
sesame = "Open Sesame"
distance = 24
previous = ""
while True:
    up = {'x': hero.pos.x, 'y': hero.pos.y + distance}
    down = {'x': hero.pos.x, 'y': hero.pos.y - distance}
    right = {'x': hero.pos.x + distance, 'y': hero.pos.y}
    left = {'x': hero.pos.x - distance, 'y': hero.pos.y}
    hero.say(sesame)
    # Check each direction to see if the path is clear.
    # Be sure to check and record your previous direction!
    # Up
    if (hero.isPathClear(hero.pos, up) and previous != 'd'):
        hero.moveXY(up.x, up.y)
        previous = 'u'
    # Right
    elif (hero.isPathClear(hero.pos, right) and previous != 'l'):
        hero.moveXY(right.x, right.y)
        previous = 'r'
    # Down
    elif (hero.isPathClear(hero.pos, down) and previous != 'u'):
        hero.moveXY(down.x, down.y)
        previous = 'd'
    # Left
    elif (hero.isPathClear(hero.pos, left) and previous != 'r'):
        hero.moveXY(left.x, left.y)
        previous = 'l'
