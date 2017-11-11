# Если крестьянин будет ранен, цветы высыхают!

def summonSoldiers():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")


# Определите функцию: commandSoldiers
def commandSoldiers():
    for soldier in hero.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)


# Определите функцию: pickUpNearestCoin
def pickUpNearestCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)


peasant = hero.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()
