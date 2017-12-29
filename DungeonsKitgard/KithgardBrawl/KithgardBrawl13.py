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
if hero.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and enemy.team != team and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
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
        elif friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandSoldier(soldier):
    hero.command(soldier, "defend", hero)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        hero.command(soldier, "move", item.pos)


def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health<hero.maxHealth):
        hero.command(paladin, "cast", "heal", self)
    else:
        hero.command(soldier, "defend", hero)


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack():
    target = findTarget()
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (hero.canCast('invisibility', self)):
            hero.cast('invisibility', self)
        elif (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        elif (hero.canCast('drain-life', target)):
            hero.cast('drain-life', target)
        elif (hero.canCast('poison-cloud', target)):
            hero.cast('poison-cloud', target)
        elif (hero.canCast('fear', target)):
            hero.cast('fear', target)
        else:
            if (hero.canCast('chain-lightning', target)):
                hero.cast('chain-lightning', target)
            elif (hero.isReady("attack")):
                hero.attack(target)


invis = -5
while True:
    commandTroops()
    if hero.now() - invis < 4:
        items = hero.findItems()
        if len(items>0):
            pickUpNearestItem(items)
        else:
            hero.move({'x':14, 'y':51})
    else:
        if (hero.canCast('earthskin', self)):
            hero.cast('earthskin', self)
        attack()
        summonTroops()

