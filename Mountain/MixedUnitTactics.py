# Practice using modulo to loop over an array

# Choose the mix and order of units you want to summon by populating this array:
summonTypes = ['archer', 'archer', 'archer', 'archer', 'archer', 'archer', 'soldier']


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


# pickup coin
def pickUpNearestItem():
    items = hero.findItems()
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = hero.findNearestEnemy()
        if enemy and (soldier.type == 'archer' or soldier.type == 'soldier'):
            hero.command(soldier, "attack", enemy)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.isReady("attack")):
            hero.attack(target)
        else:
            hero.shield()


while True:
    summonTroops()
    commandSoldiers()
    enemy = hero.findNearestEnemy()
    if (enemy and hero.distanceTo(enemy) < 10):
        attack(enemy)
    else:
        pickUpNearestItem()
