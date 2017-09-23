def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


# pickup coin
def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
summonTypes = ['griffin-rider', 'soldier', 'archer']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def findNearest(index):
    top = False
    left = False
    if (index == 0):
        top = True
        left = True
    elif (index == 1):
        top = True
    elif (index == 3):
        left = True
    items = hero.findItems()
    for item in items:
        if (item.pos.y > 66 and top and left and item.pos.x < 76):
            return item
        elif (item.pos.y < 66 and not top and left and item.pos.x < 76):
            return item
        elif (item.pos.y > 66 and top and not left and item.pos.x > 76):
            return item
        elif (item.pos.y < 66 and not top and not left and item.pos.x > 76):
            return item
    return None


# commands attack
def commandTroops():
    index = 0
    for friend in hero.findFriends():
        if friend.type == 'peasant':
            item = findNearest(index)
            index += 1
            if item:
                hero.command(friend, 'move', item.pos)
        else:
            enemy = hero.findNearestEnemy()
            if enemy:
                hero.command(friend, "attack", enemy)


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


while True:
    summonTroops()
    commandTroops()
    enemy = hero.findNearestEnemy()
    attack(enemy)
