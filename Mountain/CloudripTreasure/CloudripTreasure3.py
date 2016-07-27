# http://codecombat.com/play/level/cloudrip-treasure
# алгоритм выбора цели
def moveTo(position, fast=True):
    if (self.isReady("jump")):
        self.jumpTo(position)
    else:
        self.move(position)


# pickup coin
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
summonTypes = ['soldier', 'soldier', 'soldier', 'soldier', 'paladin']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


# commands attack
def CommandPaladin(paladin):
    if (paladin.canCast("heal") and self.health < self.maxHealth * 0.6):
        self.command(paladin, "cast", "heal", self)
    else:
        target = self.findNearest(self.findEnemies())
        self.command(paladin, "attack", target)


def сommandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)
        elif friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(paladin):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(paladin, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        self.command(soldier, "move", item.pos)


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(enemy.pos)
        elif (self.isReady("bash")):
            self.bash(enemy)
        elif (self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        else:
            self.attack(enemy)


loop:
summonTroops()
сommandTroops()
enemy = self.findNearest(self.findEnemies())
attack(enemy)
