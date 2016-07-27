# I stole this
# https://codecombat.com/play/level/treasured-in-ice
# Find the treasure inside the maze.
# When you get the treasure, move to the exit.
# The exit is marked by the red cross. The level ends when you step on the mark.
# Some doors are blocked, some open when you are near them.

exitPosition = {"x": 150, "y": 120}
hero.wait(.1)
chest = hero.findItems()[0]
walls = [[0] * 4 for i in range(100)]
steps = []


def direction(n):
    x = 0
    y = 0
    if n == 0:
        y += 16
    elif n == 1:
        x += 16
    elif n == 2:
        y -= 16
    else:
        x -= 16
    return {"x": hero.pos.x + x, "y": hero.pos.y + y}


while True:
    jMod = 0
    doNext = True
    lastStep = (steps[-1] + 2) % 4
    yDif = hero.pos.y - chest.pos.y
    xDif = hero.pos.x - chest.pos.x
    if hero.distanceTo(chest) < 5:
        break
    if yDif > 1:
        if xDif > 1:
            jMod = 2
        else:
            jMod = 1
    else:
        if xDif > 1:
            jMod = 3
    # hero.say(jMod)
    for j in range(4):
        i = (j + jMod) % 4
        checkPoint = direction(i)
        if hero.isPathClear(hero.pos, checkPoint) and walls[len(steps)][i] == 0 and i != lastStep:
            hero.moveXY(checkPoint.x, checkPoint.y)
            steps.append(i)
            doNext = False
            break
    if doNext:
        checkPoint = direction(lastStep)
        walls[len(steps) - 1][steps[-1]] = 1
        steps.pop()
        hero.moveXY(checkPoint.x, checkPoint.y)

while hero.distanceTo(exitPosition) > 10:
    checkPoint = direction((steps[-1] + 2) % 4)
    steps.pop()
    hero.moveXY(checkPoint.x, checkPoint.y)

hero.moveXY(exitPosition.x, exitPosition.y)
