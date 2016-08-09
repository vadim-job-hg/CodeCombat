enemy_types = {}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 10}
enemy_types['warlock'] = {'danger': 10, 'focus': 10}
enemy_types['arrow-tower'] = {'danger': 10, 'focus': 10}
enemy_types['burl'] = {'danger': 10, 'focus': 5}
enemy_types['witch'] = {'danger': 8, 'focus': 10}
enemy_types['brawler'] = {'danger': 7, 'focus': 10}
enemy_types['ogre'] = {'danger': 5, 'focus': 10}
enemy_types['chieftain'] = {'danger': 6, 'focus': 10}
enemy_types['fangrider'] = {'danger': 4, 'focus': 22}
enemy_types['skeleton'] = {'danger': 5, 'focus': 22}
enemy_types['scout'] = {'danger': 4, 'focus': 22}
enemy_types['thrower'] = {'danger': 3, 'focus': 22}
enemy_types['munchkin'] = {'danger': 2, 'focus': 15}
if self.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger > danger:
            enemy = self.findNearest(self.findByType(type))
            if enemy and enemy.team != team and self.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if enemy_return is None:
        enemy_return = self.findNearest(self.findEnemies())
    return enemy_return


def moveTo(position, fast=True):
    if position:
        if (self.isReady("jump") and fast):
            self.jumpTo(position)
        else:
            self.move(position)


summonTypes = ['soldier','soldier','soldier','soldier','soldier','soldier','paladin']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(soldier):
    self.command(soldier, "defend", hero)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        self.command(soldier, "move", item.pos)


def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health<hero.maxHealth):
        self.command(paladin, "cast", "heal", self)
    else:
        self.command(paladin, "defend", hero)


def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack():
    target = findTarget()
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (self.canCast('invisibility', self)):
            self.cast('invisibility', self)
        elif (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        elif (hero.canCast('drain-life', target)):
            hero.cast('drain-life', target)
        elif (hero.canCast('poison-cloud', target)):
            hero.cast('poison-cloud', target)
        elif (hero.canCast('fear', target)):
            hero.cast('fear', target)
        else:
            if (self.canCast('earthskin', self)):
                self.cast('earthskin', self)
            elif (self.canCast('chain-lightning', target)):
                self.cast('chain-lightning', target)
            elif (self.distanceTo(target) > 10):
                moveTo(target.pos)
            elif (self.isReady("attack")):
                self.attack(target)


invis = -5
loop:
    commandTroops()
    if hero.now() - invis < 4:
        items = self.findItems()
        pickUpNearestItem(items)
    else:
        if (self.canCast('earthskin', self)):
            self.cast('earthskin', self)
        attack()
        summonTroops()

