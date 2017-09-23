def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        elif (hero.isReady("attack")):
            hero.attack(target)
        else:
            hero.shield()


while True:
    items = hero.findItems()
    enemyattack = hero.findNearestEnemy()
    if enemyattack and hero.distanceTo(enemyattack) < 2:
        if (enemyattack):
            attack(enemyattack)
        else:
            hero.shield()
    else:
        if len(items) > 0:
            pickUpNearestItem(items)
