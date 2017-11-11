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


def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")


# commands attack
def commandSoldiers():
    for soldier in hero.findByType("soldier"):
        hero.command(soldier, "move", {'x': 50, 'y': 41})


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
    summonSoldier()
    commandSoldiers()
