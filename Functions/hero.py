def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


# pickup coin
def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


buildTypes = ["fire-trap", "decoy", "arrow-tower"]


def buildTroops():
    coor = coors[len(hero.built) % len(coors)]
    type = buildTypes[len(hero.built) % len(buildTypes)]
    if hero.gold > hero.costOf(type):
        hero.buildXY(type, coor[0], coor[1])


route = [[33, 14, True], [34, 7, False]]
index = 0


def moveHero():
    if len(route) > index:
        moveTo({'x': route[index][0], 'y': route[index][1]}, route[index][2])
        if (hero.pos.x == route[index][0] and hero.pos.y == route[index][1]):
            return True
        else:
            return False


if (moveHero()):
    index = index + 1


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(target)
        elif (hero.isReady("cleave")):
            hero.cleave(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)
            hero.shield()
