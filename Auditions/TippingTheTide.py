# http://codecombat.com/play/level/tipping-the-tide
# http://codecombat.com/play/level/one-level-to-rule-them-all


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def сommandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        if (self.health < self.maxHealth * 0.6):
            target = self
        if target:
            self.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        self.command(paladin, "shield")
    else:
        target = self.findNearest(self.findEnemies())
        self.command(paladin, "attack", target)


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


loop:
flag = self.findFlag()
summonTroops()
сommandTroops()
if flag:
    self.pickUpFlag(flag)
else:
    enemy = self.findNearest(self.findEnemies())
    if enemy:
        attack(enemy)
        # find some enemy to attack
        # use cleave when ready
