def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)

def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        enemies = hero.findEnemies()
        witch = hero.findNearest(hero.findByType('witch'))
        if len(enemies) > 0 and witch:
            if friend.type == 'paladin':
                CommandPaladin(friend)
            else:
                CommandSoldier(friend)
        elif hero.now() < 10 and hero.now() > 5 and friend.type == 'paladin':
            if (friend.canCast("heal")):
                hero.command(friend, "cast", "heal", friend)
            elif hero.now() < 7:
                hero.command(friend, "move", {'x': 31, 'y': 40})
            elif hero.now() < 12:
                hero.command(friend, "move", {'x': 7, 'y': 40})
        elif hero.now() < 15 and friend.type != 'archer':
            worst = findWorstEnemy()
            if (worst and friend.pos.x - worst.pos.x < 10):
                hero.command(friend, "move", {'x': 50, 'y': 58})
        elif friend.type == 'archer' and hero.now() < 15:
            if hero.now() < 7:
                hero.command(friend, "move", {'x': 6, 'y': 58})
            else:
                hero.command(friend, "move", {'x': 49, 'y': 58})
        elif hero.now() < 17:
            hero.command(friend, "move", {'x': 50, 'y': 39})
        else:
            hero.command(friend, "move", {'x': 78, 'y': 40})


def CommandPaladin(paladin):
    if (paladin.canCast("heal")):
        target = lowestHealthFriend()
        if target:
            hero.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        hero.command(paladin, "shield")
    else:
        target = findWorstEnemy()
        if (target):
            hero.command(paladin, "attack", target)

def CommandSoldier(soldier):
    target = findWorstEnemy()
    if (target):
        hero.command(soldier, "attack", target)

def findWorstEnemy():
    witch = hero.findNearest(hero.findByType('witch'))
    ogre = hero.findNearest(hero.findByType('ogre'))
    skeleton = hero.findNearest(hero.findByType('skeleton'))
    if witch:
        return witch
    elif ogre:
        return ogre
    elif skeleton:
        return skeleton
    else:
        return None

def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend

def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        else:
            hero.attack(target)

while True:
    commandTroops()
    brawler = hero.findNearest(hero.findByType('brawler'))
    catapult = hero.findNearest(hero.findByType('catapult'))
    if brawler and hero.distanceTo(brawler) > 15:
        moveTo(brawler.pos, False)
    elif brawler:
        runaway = Vector.subtract(hero.pos, brawler.pos)
        runaway = Vector.normalize(runaway)
        runaway = Vector.multiply(runaway, 15)
        direction = Vector.add(runaway, hero.pos)
        moveTo(direction, False)
    elif catapult:
        attack(catapult)
    else:
        hero.move({'x': 78, 'y': 15})