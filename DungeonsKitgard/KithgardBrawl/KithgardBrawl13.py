def moveTo(position, fast=True):
    if (self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(soldier):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(soldier, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        self.command(soldier, "move", item.pos)


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        self.command(paladin, "cast", "heal", self)
    else:
        self.command(paladin, "shield")


def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack(target):
    if target:
        if (self.distanceTo(target) < 10 and self.isReady("bash")):
            self.bash(target)


buildTypes = ["fire-trap", "decoy"]


def buildTroops():
    enemy = self.findNearest(self.findEnemies())
    items = self.findItems()
    if enemy:
        pass
        # if(self.isReady("bash")):
        #    self.bash(enemy)
        # elif(self.canCast('chain-lightning', enemy)):
        #    self.cast('chain-lightning', enemy)
    paladins = self.findByType('paladin')
    if len(items) > 0 and hero.distanceTo(items[0]) < 10:
        pickUpNearestItem(items)
    elif len(paladins) > 1:
        self.shield()
    elif enemy and self.distanceTo(enemy) < 10:
        type = buildTypes[len(self.built) % len(buildTypes)]
        if self.gold > self.costOf(type):
            self.buildXY(type, enemy.pos.x, enemy.pos.y)
            self.shield()
            self.shield()
        else:
            pickUpNearestItem(items)
    else:
        pickUpNearestItem(items)


while True:
    commandTroops()
    if (self.canCast('invisibility', self)):
        self.cast('invisibility', self)
    elif self.hasEffect('invisibility'):
        self.shield()
    else:
        if (self.canCast('earthskin', self)):
            self.cast('earthskin', self)
        buildTroops()
        if self.health < self.maxHealth * 0.6:
            paladins = self.findByType('paladin')
            if len(paladins) == 0:
                summonTroops()
                summonTroops()
