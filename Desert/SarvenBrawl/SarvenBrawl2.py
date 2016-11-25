def pickUpNearestCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)


def attack(target):
    if target:
        if (hero.isReady("jump") and hero.distanceTo > 10):
            hero.jumpTo(enemy.pos)
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
    for soldier in hero.findByType("soldier"):
        hero.command(soldier, "defend", self)


while True:
    enemies = hero.findEnemies()
    index = 0
    distanse = 99999
    enemy = None
    while index < len(enemies):
        if enemies[index].type != "sand-yak" and distanse > hero.distanceTo(enemies[index]):
            distanse = hero.distanceTo(enemies[index])
            enemy = enemies[index]
        index += 1
    items = hero.findItems()
    if len(items) > 0:
        pickUpNearestCoin()
    if enemy is not None and enemy.type != "sand-yak":
        if (hero.distanceTo(enemy) < 7):
            attack(enemy)
        elif (hero.distanceTo(enemy) < 20):
            if (hero.isReady("jump") and hero.distanceTo > 10):
                hero.jumpTo(enemy.pos)
            else:
                hero.move(enemy.pos)
        else:
            hero.move({'x': 89, 'y': 72})
    summonTroops()
    commandSoldiers()
