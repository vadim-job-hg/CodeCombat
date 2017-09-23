enemy_types = {}
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
enemy_types['soldier'] = {'danger': 90, 'focus': 50}
enemy_types['skeleton'] = {'danger': 90, 'focus': 50}
enemy_types['griffin-rider'] = {'danger': 99, 'focus': 50}
enemy_types['paladin'] = {'danger': 99, 'focus': 50}
enemy_types['burl'] = {'danger': 99, 'focus': 50}
enemy_types['archer'] = {'danger': 50, 'focus': 50}
def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    return enemy_return


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and enemy.team != hero.team and hero.distanceTo(enemy) < enemy_types[type].focus:
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
        elif friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider' or friend.type == 'skeleton':
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
        hero.command(paladin, "defend", hero)


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack():
    target = findTarget()
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        if (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        if (hero.canCast('invisibility', self)):
            hero.cast('invisibility', self)
        if (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        if(hero.isReady("throw") and hero.distanceTo(target)<hero.trowRange):
            hero.trow(target)
        elif (hero.canCast('poison-cloud', target)):
            hero.cast('poison-cloud', target)
        elif (hero.canCast('fear', target)):
            hero.cast('fear', target)
        else:
            if (hero.canCast('earthskin', self)):
                hero.cast('earthskin', self)
            elif (hero.canCast('chain-lightning', target)):
                hero.cast('chain-lightning', target)
            elif (hero.distanceTo(target) > 100):
                moveTo(target.pos)
            #elif (hero.canCast('drain-life', target)):
            #    hero.cast('drain-life', target)
            elif (hero.isReady("attack")):
                hero.attack(target)


invis = -5
while True:
    commandTroops()
    if hero.now() - invis < 4:
        items = hero.findItems()
        pickUpNearestItem(items)
    else:
        if (hero.canCast('earthskin', self)):
            hero.cast('earthskin', self)
        attack()
        summonTroops()
