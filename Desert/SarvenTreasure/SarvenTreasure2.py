def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack(target):
    if target:
        if (hero.distanceTo(target) < 10 and hero.isReady("bash")):
            hero.bash(target)


index = 0
route = [[7, 19, True, [5, 20]], [75, 19, True, [77, 20]]]


def moveHero():
    ind = index % len(route)
    moveTo({'x': route[ind][0], 'y': route[ind][1]}, route[ind][2])
    if (hero.pos.x == route[ind][0] and hero.pos.y == route[ind][1]):
        # hero.say(route[ind][3]);
        hero.moveXY(route[ind][3][0], route[ind][3][1])
        return True
    else:
        return False


while True:
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    items = hero.findItems()
    item = hero.findNearest(items)
    if enemy and hero.distanceTo(enemy) > 10 and items and (item.pos.x < 30 or item.pos.x > 60):
        pickUpNearestItem(items)
    elif(enemy and hero.isReady("bash")):
        hero.bash(enemy)
    elif(enemy and hero.canCast('chain-lightning', enemy)):
        hero.cast('chain-lightning', enemy)
    elif (moveHero()):
        index = index + 1
