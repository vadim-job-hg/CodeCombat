enemy_types = {}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 10}
enemy_types['warlock'] = {'danger': 10, 'focus': 10}
enemy_types['burl'] = {'danger': 10, 'focus': 5}
enemy_types['witch'] = {'danger': 8, 'focus': 10}
enemy_types['brawler'] = {'danger': 7, 'focus': 10}
enemy_types['ogre'] = {'danger': 5, 'focus': 10}
enemy_types['chieftain'] = {'danger': 6, 'focus': 10}
if self.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
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
        elif friend.type == 'soldier':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(soldier):
    #target = self.findNearest(self.findEnemies())
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


def attack():
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (hero.canCast('poison-cloud', target)):
            hero.cast('poison-cloud', target)
        elif (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        elif (hero.canCast('drain-life', target)):
            hero.cast('drain-life', target)
        elif (hero.canCast('fear', target)):
            hero.cast('fear', target)
        elif (self.canCast('invisibility', self)):
            self.cast('invisibility', self)
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
while True:
    target = findTarget()
    commandTroops()
    if (self.canCast('invisibility', self)):
        self.cast('invisibility', self)
        invis = hero.now()
    else:
        if (self.canCast('earthskin', self)):
            self.cast('earthskin', self)
        attack()
        summonTroops()

