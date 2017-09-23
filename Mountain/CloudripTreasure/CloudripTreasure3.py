# http://codecombat.com/play/level/cloudrip-treasure
# алгоритм выбора цели
def moveTo(position, fast=True):
    if (hero.isReady("jump")):
        hero.jumpTo(position)
    else:
        hero.move(position)


# pickup coin
def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
summonTypes = ['soldier', 'soldier', 'soldier', 'soldier', 'paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


# commands attack
def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health < hero.maxHealth * 0.6):
        hero.command(paladin, "cast", "heal", self)
    else:
        target = hero.findNearestEnemy()
        hero.command(paladin, "attack", target)


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


def CommandSoldier(paladin):
    target = hero.findNearestEnemy()
    if target:
        hero.command(paladin, "attack", target)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        hero.command(soldier, "move", item.pos)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(enemy.pos)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(enemy)


while True:
    summonTroops()
    commandTroops()
    enemy = hero.findNearestEnemy()
    attack(enemy)
