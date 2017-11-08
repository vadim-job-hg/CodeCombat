summonTypes = ['griffin-rider']
tactick = 'hold'
stage = 1


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend
    return lowestFriend


def commandPaladin(paladin):
    if (paladin.canCast("heal")):
        if (hero.health < hero.maxHealth * 0.8):
            target = self
        else:
            target = lowestHealthPaladin()
        if target:
            hero.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        hero.command(paladin, "shield")
    elif stage < 4:
        hero.command(paladin, "move", {'x': 94, 'y': 34})
    elif stage == 5:
        hero.command(paladin, "move", {'x': 284, 'y': 33})
    else:
        target = hero.findNearestEnemy()
        if (warlock):
            target = warlock
        if (target):
            hero.command(paladin, "attack", target)


def commandSoldier(soldier):
    target = hero.findNearestEnemy()
    if (warlock):
        target = warlock
    if stage == 3:
        hero.command(soldier, "move", {'x': 84, 'y': 34})
    elif (target):
        hero.command(soldier, "attack", target)


def commandFriends():
    friends = hero.findFriends()
    for friend in friends:
        if tactick == 'hold':
            hero.command(friend, "defend", {'x': 1, 'y': 40})
        elif friend.type == "paladin":
            commandPaladin(friend)
        else:
            commandSoldier(friend)


def moveTo(position):
    if (hero.isReady("jump")):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        else:
            hero.attack(target)


def pickUpNearestItem():
    nearestItem = hero.findNearestItem()
    if nearestItem:
        moveTo(nearestItem.pos)


commandFriends()
hero.moveXY(31, 56)
while True:
    catapult = hero.findNearest(hero.findByType('catapult'))
    warlock = hero.findNearest(hero.findByType('warlock'))
    target = hero.findNearestEnemy()
    nearestItem = hero.findNearestItem()
    now = hero.now()
    if catapult:
        stage = 1
        attack(catapult)
    elif now < 20:
        tactick = 'defend'
        stage = 2
        moveTo({"x": 50, "y": 33})
    elif stage < 4:
        if target:
            stage = 3
            attack(target)
        else:
            moveTo({"x": 172, "y": 46})
        if hero.pos.x > 170:
            stage = 4
    elif stage < 5:
        if hero.pos.x < 240:
            moveTo({"x": 274, "y": 35})
            tactick = 'defend'
        elif nearestItem and hero.distanceTo(nearestItem) < 10:
            pickUpNearestItem()
            tactick = 'attack'
        elif (warlock):
            target = warlock
            summonTroops()
            attack(target)
        elif target and target.type != 'gates':
            attack(target)
        elif nearestItem and hero.distanceTo(nearestItem) < 45:
            pickUpNearestItem()
            tactick = 'defend'
            summonTroops()
        else:
            attack(target)
        if hero.pos.x > 290:
            stage = 5
        tactick = 'attack'
    else:
        summonTroops()
        attack(target)
    commandFriends()
