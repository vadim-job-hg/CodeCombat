# https://codecombat.com/play/level/kithgards-secret
# Should fill in some default source
enemy_types = {}
enemy_types['fangrider'] = {'danger': 4, 'focus': 100}


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
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


summonTypes = ['paladin', 'paladin', 'paladin', 'paladin']


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
    if enemyattack:
        hero.command(soldier, "attack", enemyattack)


def CommandSoldier(soldier):
    pass


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


while True:
    summonTroops()
    commandTroops()
    items = hero.findItems()
    enimies = hero.findEnemies()
    # for enemy in enimies:
    #    hero.say(enemy.type)
    if (len(items) > 0 and hero.health < hero.maxHealth * 0.5):
        pickUpNearestItem(items)
    else:
        enemyattack = findTarget()
        if not enemyattack:
            enemyattack = hero.findNearestEnemy()
        if (enemyattack and False):
            attack(enemyattack)
        else:
            hero.shield()
