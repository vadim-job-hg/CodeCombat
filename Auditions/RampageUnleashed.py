# http://codecombat.com/play/level/rampage-unleashed

enemy_types = {}
# humans hero types
enemy_types['knight'] = {'danger': 100, 'focus': 100}
enemy_types['ranger'] = {'danger': 100, 'focus': 100}
enemy_types['librarian'] = {'danger': 100, 'focus': 100}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['trapper'] = {'danger': 100, 'focus': 100}
enemy_types['samurai'] = {'danger': 100, 'focus': 50}
enemy_types['forest-archer'] = {'danger': 100, 'focus': 50}
enemy_types['sorcerer'] = {'danger': 100, 'focus': 50}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 100}
enemy_types['warlock'] = {'danger': 10, 'focus': 30}
enemy_types['arrow-tower'] = {'danger': 10, 'focus': 20}
enemy_types['catapult'] = {'danger': 10, 'focus': 100}
enemy_types['burl'] = {'danger': 10, 'focus': 20}
enemy_types['artillery'] = {'danger': 10, 'focus': 100}
enemy_types['witch'] = {'danger': 8, 'focus': 100}
enemy_types['brawler'] = {'danger': 7, 'focus': 55}
enemy_types['ogre'] = {'danger': 5, 'focus': 40}
enemy_types['chieftain'] = {'danger': 6, 'focus': 35}
enemy_types['fangrider'] = {'danger': 4, 'focus': 22}
enemy_types['skeleton'] = {'danger': 5, 'focus': 22}
enemy_types['scout'] = {'danger': 4, 'focus': 22}
enemy_types['thrower'] = {'danger': 3, 'focus': 22}
enemy_types['munchkin'] = {'danger': 2, 'focus': 15}
enemy_types['yak'] = {'danger': -1, 'focus': 0}
enemy_types['ice-yak'] = {'danger': -1, 'focus': 0}


def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


if self.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
            enemy = self.findNearest(self.findByType(type))
            if enemy and enemy.team != team and self.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if enemy_return is None:
        enemy_return = self.findNearest(self.findEnemies())
    return enemy_return


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)
        else:
            CommandSoldier(friend)


def CommandSoldier(soldier):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(soldier, "attack", target)


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        if (self.health < self.maxHealth * 0.6):
            target = self
        if target:
            self.command(paladin, "cast", "heal", target)
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
        else:
            self.attack(target)


while True:
    flag = self.findFlag()
    summonTroops()
    commandTroops()
    if flag:
        self.pickUpFlag(flag)
    else:
        enemy = findTarget()
        if enemy:
            attack(enemy)
        else:
            items = self.findItems()
            pickUpNearestItem(items)
            # find some enemy to attack
            # use cleave when ready
