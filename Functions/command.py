summonTypes = ['griffin-rider', 'soldier', 'archer', 'paladin', 'peasant']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


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


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        if (self.health < self.maxHealth * 0.6):
            target = self
        else:
            target = lowestHealthPaladin()
        if target:
            self.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        self.command(paladin, "shield")
    else:
        target = self.findNearest(self.findEnemies())
        self.command(paladin, "attack", target)


def CommandSoldier(soldier):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(soldier, "attack", target)


def CommandArcher(soldier):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(soldier, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        self.command(soldier, "move", item.pos)


def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend
