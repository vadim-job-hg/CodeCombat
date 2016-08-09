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


summonTypes = ['soldier', 'soldier', 'griffin-rider', 'soldier', 'archer']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


# commands attack
def commandSoldiers():
    for soldier in self.findFriends():
        if enemy:
            self.command(soldier, "attack", enemy)


loop:
summonTroops()
commandSoldiers()
items = self.findItems()
enemy = self.findNearest(self.findEnemies())
if (len(items) > 0 or (enemy and self.distanceTo(enemy) > 10)):
    pickUpNearestItem(items)
else:
    attack(enemy)
