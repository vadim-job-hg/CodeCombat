summonTypes = ['griffin-rider', 'soldier', 'archer', 'paladin', 'peasant']


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
    if (paladin.canCast("heal")):
        if (hero.health < hero.maxHealth * 0.6):
            target = self
        else:
            target = lowestHealthPaladin()
        if target:
            hero.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        hero.command(paladin, "shield")
    else:
        target = hero.findNearestEnemy()
        hero.command(paladin, "attack", target)


def CommandSoldier(soldier):
    target = hero.findNearestEnemy()
    if target:
        hero.command(soldier, "attack", target)


def CommandArcher(soldier):
    target = hero.findNearestEnemy()
    if target:
        hero.command(soldier, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        hero.command(soldier, "move", item.pos)


def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend
