def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def action():
        target = hero.findNearestEnemy()
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (target and hero.canCast('fear', target)):
            hero.cast('fear', target)
while True:
    items = hero.findItems()
    action()
    if len(items) > 0:
        pickUpNearestItem(items)
