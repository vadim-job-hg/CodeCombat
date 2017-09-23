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


def summonSoldier():
    if hero.gold > hero.costOf('archer') * 3:
        hero.summon('archer')
        hero.summon('archer')
        hero.summon('archer')


# commands attack
def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)


while True:
    summonSoldier()
    commandSoldiers()
    items = hero.findItems()
    if (len(items) > 0):
        pickUpNearestItem(items)
    else:
        enemy = hero.findNearestEnemy()
        attack(enemy)
