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
    if hero.gold > hero.costOf('soldier'):
        hero.summon('soldier')


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
        if (enemy and hero.distanceTo(enemy) < 10):
            attack(enemy)
        elif (hero.pos.x != 13 and hero.pos.y != 51):
            moveTo({'x': 13, 'y': 51})
        else:
            hero.shield()
