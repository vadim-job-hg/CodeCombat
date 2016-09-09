enemy_types = {}
enemy_types['door'] = {'danger': 1000, 'focus': 200}
enemy_types['knight'] = {'danger': 100, 'focus': 100}
enemy_types['potion-master'] = {'danger': 100, 'focus': 100}
enemy_types['ranger'] = {'danger': 100, 'focus': 100}
enemy_types['trapper'] = {'danger': 100, 'focus': 100}
enemy_types['samurai'] = {'danger': 100, 'focus': 100}
enemy_types['librarian'] = {'danger': 100, 'focus': 100}
enemy_types['sorcerer'] = {'danger': 100, 'focus': 100}
enemy_types['hero-placeholder'] = {'danger': 99, 'focus': 100}
enemy_types['hero-placeholder-1'] = {'danger': 99, 'focus': 100}
enemy_types['hero-placeholder-2'] = {'danger': 99, 'focus': 100}
enemy_types['necromancer'] = {'danger': 100, 'focus': 100}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['goliath'] = {'danger': 100, 'focus': 50}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['forest-archer'] = {'danger': 100, 'focus': 50}
enemy_types['ninja'] = {'danger': 100, 'focus': 50}

def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger > danger:
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
        if (self.canCast('invisibility', self)):
            self.cast('invisibility', self)
        elif self.hasEffect('invisibility'):
            moveTo(target.pos)
        else:
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


summonTypes = ['paladin']


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
    if (paladin.canCast("heal") and self.health < self.maxHealth * 0.6):
        self.command(paladin, "cast", "heal", self)
    else:
        enemyattack = findTarget()
        if enemyattack:
            self.command(paladin, "shield")
        else:
            self.command(paladin, "shield")


def CommandSoldier(soldier):
    self.command(soldier, "defend", self)


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
if (self.canCast('invisibility', self)):
    self.cast('invisibility', self)
while True:
    items = self.findItems()
    enimies = self.findEnemies()
    if (len(items) > 0 and self.health < self.maxHealth * 0.5):
        pickUpNearestItem(items)
    else:
        enemyattack = findTarget()
        if (enemyattack and hero.now()<30):
            attack(enemyattack)
        else:
            if (self.canCast('invisibility', self)):
                self.cast('invisibility', self)
            self.shield()
    if hero.health<1000:
        summonTroops()
    commandTroops()
