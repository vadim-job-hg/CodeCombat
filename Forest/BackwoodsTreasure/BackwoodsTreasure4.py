def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


summonTypes = ['paladin']


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
    target = hero.findNearestEnemy()
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


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack(target):
    if target:
        if (hero.distanceTo(target) < 10 and hero.isReady("bash")):
            hero.bash(target)


buildTypes = ["fire-trap"]


def buildTroops():
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    items = hero.findItems()
    if enemy and len(enemies) > 2 and hero.distanceTo(enemy) < 10:
        type = "fire-trap"
        if hero.gold > 10:
            hero.buildXY(type, enemy.pos.x, enemy.pos.y)
            hero.shield()
            hero.shield()
            hero.shield()
            hero.shield()
            hero.shield()
        else:
            pickUpNearestItem(items)
    elif enemy and len(enemies) == 0:
        type = "arrow-tower"
        if hero.gold > 60:
            hero.buildXY(type, hero.pos.x, hero.pos.y)
        else:
            pickUpNearestItem(items)
    else:
        pickUpNearestItem(items)


while True:
    buildTroops()
