# https://codecombat.com/play/level/kithgards-secret
# Should fill in some default source
enemy_types = {}
enemy_types['fangrider'] = {'danger': 4, 'focus': 100}


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
            enemy = self.findNearest(self.findByType(type))
            if enemy and self.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    return enemy_return


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


summonTypes = ['paladin', 'paladin', 'paladin', 'paladin']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def commandTroops():
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
    if enemyattack:
        self.command(soldier, "attack", enemyattack)


def CommandSoldier(soldier):
    pass


def CommandArcher(soldier):
    if enemyattack:
        self.command(soldier, "attack", enemyattack)


def CommandPeasant(soldier):
    if enemyattack:
        self.command(soldier, "attack", enemyattack)


def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend


while True:
    summonTroops()
    commandTroops()
    items = self.findItems()
    enimies = self.findEnemies()
    # for enemy in enimies:
    #    self.say(enemy.type)
    if (len(items) > 0 and self.health < self.maxHealth * 0.5):
        pickUpNearestItem(items)
    else:
        enemyattack = findTarget()
        if not enemyattack:
            enemyattack = self.findNearest(self.findEnemies())
        if (enemyattack and False):
            attack(enemyattack)
        else:
            self.shield()
