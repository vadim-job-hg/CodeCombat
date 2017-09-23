enemy_types = {}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 10}
enemy_types['warlock'] = {'danger': 10, 'focus': 10}
enemy_types['burl'] = {'danger': 10, 'focus': 5}
enemy_types['witch'] = {'danger': 8, 'focus': 10}
enemy_types['brawler'] = {'danger': 7, 'focus': 10}
enemy_types['ogre'] = {'danger': 5, 'focus': 10}
enemy_types['chieftain'] = {'danger': 6, 'focus': 10}
if hero.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
    if enemy_return is None:
        enemy_return = hero.findNearestEnemy()
    return enemy_return


def moveTo(position, fast=True):
    if position:
        if (hero.isReady("jump") and fast):
            hero.jumpTo(position)
        else:
            hero.move(position)


summonTypes = ['soldier','soldier','soldier','soldier','soldier','soldier','paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(soldier):
    #target = hero.findNearestEnemy()
    if target:
        hero.command(soldier, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        hero.command(soldier, "move", item.pos)


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        hero.command(paladin, "cast", "heal", self)
    else:
        hero.command(paladin, "shield")


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
        elif (hero.canCast('invisibility', self)):
            hero.cast('invisibility', self)
        else:
            if (hero.canCast('earthskin', self)):
                hero.cast('earthskin', self)
            elif (hero.canCast('chain-lightning', target)):
                hero.cast('chain-lightning', target)
            elif (hero.distanceTo(target) > 10):
                moveTo(target.pos)
            elif (hero.isReady("attack")):
                hero.attack(target)


invis = -5
while True:
    target = findTarget()
    commandTroops()
    if (hero.canCast('invisibility', self)):
        hero.cast('invisibility', self)
        invis = hero.now()
    else:
        if (hero.canCast('earthskin', self)):
            hero.cast('earthskin', self)
        attack()
        summonTroops()

