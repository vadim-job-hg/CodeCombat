# http://codecombat.com/play/level/sarven-siege
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


summonTypes = ['griffin-rider', 'soldier', 'archer']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


# commands attack
def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = hero.findNearestEnemy()
        if enemy and soldier.type != 'arrow-tower':
            hero.command(soldier, "attack", enemy)


while True:
    summonTroops()
    commandSoldiers()
    items = hero.findItems()
    enemy = hero.findNearestEnemy()
    if (enemy and (hero.now() > 45 or hero.distanceTo(enemy) < 20)):
        attack(enemy)
    else:
        pickUpNearestItem(items)
