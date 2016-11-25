# http://codecombat.com/play/level/grim-determination
summonTypes = ['griffin-rider']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


# Найти паладина с самым низким количеством здоровья.
def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend


def commandPaladin(paladin):
    if (paladin.canCast("heal")):
        target = lowestHealthPaladin()
        if target:
            hero.command(paladin, "cast", "heal", target)
    elif (paladin.health < 200):
        hero.command(paladin, "shield")
    else:
        target = paladin.findNearestEnemy()
        if (target):
            hero.command(paladin, "attack", target)


def commandPeasant(peasant):
    item = peasant.findNearestItem()
    if item:
        hero.command(peasant, 'move', item.pos)


def commandGriffin(griffin):
    target = hero.findNearest(hero.findByType('warlock'))
    if not target:
        target = griffin.findNearestEnemy()
    if (target):
        hero.command(griffin, "attack", target)


def commandFriends():
    # Командуй своими союзниками.
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            commandPeasant(friend)
        elif friend.type == "griffin-rider":
            commandGriffin(friend)
        elif friend.type == "paladin":
            commandPaladin(friend)


while True:
    commandFriends()
    summonTroops()
