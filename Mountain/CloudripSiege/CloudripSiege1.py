def moveTo(position, fast=True):
    if (self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)


# pickup coin
def pickUpNearestItem():
    items = self.findItems()
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
coors = [[67, 41], [24, 54], [69, 55], [25, 34], [69, 32]]
buildTypes = ['arrow-tower']


def buildTroops():
    coor = coors[len(self.built) % len(coors)]
    type = buildTypes[len(self.built) % len(buildTypes)]
    if self.gold > self.costOf(type):
        self.buildXY(type, coor[0], coor[1])


loop:
pickUpNearestItem()
buildTroops()
