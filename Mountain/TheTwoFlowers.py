# Если крестьянин будет ранен, цветы высыхают!

def summonSoldiers():
    if self.gold >= self.costOf("soldier"):
        self.summon("soldier")


# Определите функцию: commandSoldiers
def commandSoldiers():
    for soldier in self.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            self.command(soldier, "attack", enemy)


# Определите функцию: pickUpNearestCoin
def pickUpNearestCoin():
    items = self.findItems()
    nearestCoin = self.findNearest(items)
    if nearestCoin:
        self.move(nearestCoin.pos)


peasant = self.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()
