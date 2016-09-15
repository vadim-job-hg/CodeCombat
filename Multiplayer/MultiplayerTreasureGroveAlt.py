# todo: use peasant here
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo(position) > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


def action():
        target = self.findNearest(self.findEnemies())
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (target and hero.canCast('fear', target)):
            hero.cast('fear', target)
while True:
    items = self.findItems()
    action()
    if len(items) > 0:
        pickUpNearestItem(items)
