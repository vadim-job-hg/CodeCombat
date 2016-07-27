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


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (self.isReady("bash")):
            self.bash(target)
        elif (self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        elif (self.isReady("attack")):
            self.attack(target)
        else:
            self.shield()


loop:
items = self.findItems()
enemyattack = self.findNearest(self.findEnemies())
if enemyattack and self.distanceTo(enemyattack) < 2:
    if (enemyattack):
        attack(enemyattack)
    else:
        self.shield()
else:
    if len(items) > 0:
        pickUpNearestItem(items)
