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
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    return enemy_return


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.canCast('invisibility', self)):
            hero.cast('invisibility', self)
        elif hero.hasEffect('invisibility'):
            moveTo(target.pos)
        else:
            if (hero.distanceTo(target) > 10):
                moveTo(target.pos)
            elif (hero.isReady("bash")):
                hero.bash(target)
            elif (hero.canCast('chain-lightning', target)):
                hero.cast('chain-lightning', target)
            elif (hero.isReady("attack")):
                hero.attack(target)
            else:
                hero.shield()


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)
        elif friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)


def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health < hero.maxHealth * 0.6):
        hero.command(paladin, "cast", "heal", self)
    else:
        enemyattack = findTarget()
        if enemyattack:
            hero.command(paladin, "shield")
        else:
            hero.command(paladin, "shield")


def CommandSoldier(soldier):
    hero.command(soldier, "defend", self)


def CommandArcher(soldier):
    if enemyattack:
        hero.command(soldier, "attack", enemyattack)


def CommandPeasant(soldier):
    if enemyattack:
        hero.command(soldier, "attack", enemyattack)


def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend
if (hero.canCast('invisibility', self)):
    hero.cast('invisibility', self)
while True:
    items = hero.findItems()
    enimies = hero.findEnemies()
    if (len(items) > 0 and hero.health < hero.maxHealth * 0.5):
        pickUpNearestItem(items)
    else:
        enemyattack = findTarget()
        if (enemyattack and hero.now()<30):
            attack(enemyattack)
        else:
            if (hero.canCast('invisibility', self)):
                hero.cast('invisibility', self)
            hero.shield()
    if hero.health<1000:
        summonTroops()
    commandTroops()
