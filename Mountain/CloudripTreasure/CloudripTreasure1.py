def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


# pickup coin
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
summonTypes = ['griffin-rider', 'soldier', 'archer']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def findNearest(index):
    top = False
    left = False
    if (index == 0):
        top = True
        left = True
    elif (index == 1):
        top = True
    elif (index == 3):
        left = True
    items = self.findItems()
    for item in items:
        if (item.pos.y > 66 and top and left and item.pos.x < 76):
            return item
        elif (item.pos.y < 66 and not top and left and item.pos.x < 76):
            return item
        elif (item.pos.y > 66 and top and not left and item.pos.x > 76):
            return item
        elif (item.pos.y < 66 and not top and not left and item.pos.x > 76):
            return item
    return None


# commands attack
def commandTroops():
    index = 0
    for friend in self.findFriends():
        if friend.type == 'peasant':
            item = findNearest(index)
            index += 1
            if item:
                self.command(friend, 'move', item.pos)
        else:
            enemy = self.findNearest(self.findEnemies())
            if enemy:
                self.command(friend, "attack", enemy)


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


loop:
summonTroops()
commandTroops()
enemy = self.findNearest(self.findEnemies())
attack(enemy)
