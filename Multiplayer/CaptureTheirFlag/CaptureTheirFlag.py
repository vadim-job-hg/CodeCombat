# http://codecombat.com/play/ladder/capture-their-flag

# For this level you will have 3 main functions that you need to use.
# placeFlag - this should be called three times at the beginning of your code to hide your 3 flags
def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


route = [[128, 36, True], [75, 66, False], [129, 82, False], [80, 103, False], [129, 107, False]]
index = 0


def moveHero():
    if len(route) > index:
        moveTo({'x': route[index][0], 'y': route[index][1]}, route[index][2])
        if (hero.pos.x == route[index][0] and hero.pos.y == route[index][1]):
            return True
        else:
            return False


hero.placeFlag({'x': 20, 'y': 60})
hero.placeFlag({'x': -6, 'y': 109})
hero.placeFlag({'x': -7, 'y': 9})
hero.moveXY(121, 46)
while True:
    target = None
    flags = hero.findByType('flag')
    for flag in flags:
        if flag.team == 'ogres':
            target = flag
            break
    if target and hero.distanceTo(target) < 3:
        flag = hero.findEnemyFlags()
        hero.captureFlag(flag[0])
    elif len(flag) > 0 and hero.distanceTo(target) > 3:
        hero.move(target)
    elif (moveHero()):
        index = index + 1  # findEnemyFlags - this should be called in order to locate enemy flags, it returns an array of any enemy flag within 5 units of you
    # captureFlag - this is called on a flag you've found and captures it if you are within 3 units of the flag, then you can run the flag back to your side of the map
    # you also have the ability to control your robot-walker, though he can only fire, not move
