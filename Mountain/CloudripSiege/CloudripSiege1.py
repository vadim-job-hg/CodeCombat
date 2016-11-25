def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


# pickup coin
def pickUpNearestItem():
    items = hero.findItems()
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
coors = [[67, 41], [24, 54], [69, 55], [25, 34], [69, 32]]
buildTypes = ['arrow-tower']


def buildTroops():
    coor = coors[len(hero.built) % len(coors)]
    type = buildTypes[len(hero.built) % len(buildTypes)]
    if hero.gold > hero.costOf(type):
        hero.buildXY(type, coor[0], coor[1])


while True:
    pickUpNearestItem()
    buildTroops()
