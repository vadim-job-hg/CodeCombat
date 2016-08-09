def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(enemy.pos)
        elif (self.isReady("bash")):
            self.bash(enemy)
        elif (self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif (self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.attack(enemy)


def summonSoldier():
    if self.gold > self.costOf('archer') * 3:
        self.summon('archer')
        self.summon('archer')
        self.summon('archer')


# commands attack
def commandSoldiers():
    for soldier in self.findFriends():
        enemy = self.findNearest(self.findEnemies())
        if enemy:
            self.command(soldier, "attack", enemy)


loop:
summonSoldier()
commandSoldiers()
items = self.findItems()
if (len(items) > 0):
    pickUpNearestItem(items)
else:
    enemy = self.findNearest(self.findEnemies())
    attack(enemy)
