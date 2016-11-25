# Get all your troops to the end of the path by passing over the mines.
# You can locate duds by finding the mines that have a value that is a prime number.
# Check the guide for clarification.
route = [[6, 41, 0], [3, 16, 1], [79, 5, 0], [91, 12, 1], [82, 62, 0], [81, 62, 0], [80, 62, 0], [79, 62, 0],
         [78, 62, 0], [78, 62, 0], [77, 62, 0]]
routeIndex = 0;
SafeWay = [[70, 40]]
SafeWayIndex = 1


def moveTroop():
    moved = True
    for index, friend in enumerate(hero.findFriends()):
        ind = SafeWayIndex - index
        if ind >= 0 and ind < len(SafeWay):
            if friend.pos.x != SafeWay[ind][0] or friend.pos.y != SafeWay[ind][1]:
                moved = False
                hero.command(friend, 'move', {'x': SafeWay[ind][0], 'y': SafeWay[ind][1]})
    return moved


def checkprimary(value):
    for j in range(2, Math.ceil(Math.sqrt(value))):
        if value % j == 0:
            return False
    return True


def checkifExist(object):
    for wayEl in SafeWay:
        if object.pos.x == wayEl[0] and object.pos.y == wayEl[1]:
            return False
    return True


def checktrap():
    objects = hero.findHazards()
    for object in objects:
        if (hero.distanceTo(object) < 20 and checkifExist(object) and checkprimary(object.value)):
            hero.moveXY(object.pos.x, object.pos.y)
            SafeWay.push([object.pos.x, object.pos.y])
            return True
    return False


while True:
    checktrap()
    if routeIndex < len(route):
        if route[routeIndex][2] == 1:
            hero.moveXY(route[routeIndex][0], route[routeIndex][1])
            SafeWay.push(route[routeIndex])
            routeIndex = routeIndex + 1
        else:
            hero.move({'x': route[routeIndex][0], 'y': route[routeIndex][1]})
            if hero.pos.x == route[routeIndex][0] and hero.pos.y == route[routeIndex][1]:
                SafeWay.push(route[routeIndex])
                routeIndex = routeIndex + 1

    if moveTroop():
        SafeWayIndex = SafeWayIndex + 1
