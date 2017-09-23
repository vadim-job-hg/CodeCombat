def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(enemy.pos)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        elif (hero.isReady("cleave")):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)


def summonSoldier(lenlist):
    soldier = 'archer'
    if hero.gold > hero.costOf(soldier):
        hero.summon(soldier)
        indexSoldier += 1


# commands attack
def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = hero.findNearestEnemy()
        if enemy and soldier.type == 'archer':
            hero.command(soldier, "attack", enemy)


list = ['soldier', 'archer']
indexSoldier = len(list)
while True:
    if hero.now() > 10:
        summonSoldier(len(list))
    commandSoldiers()
    items = hero.findItems()
    if (len(items) > 0):
        pickUpNearestItem(items)
    else:
        enemy = hero.findNearestEnemy()
        attack(enemy)
