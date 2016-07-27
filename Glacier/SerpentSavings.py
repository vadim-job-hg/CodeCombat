# http://codecombat.com/play/level/serpent-savings
# todo this logic need to be improved
# You cannot collect coins.
# Summon peasants to collect coins for you.
# Collecting coins spawns a growing 'tail' behind the peasants.
# When a peasant touches a tail, they die.
# Collect 500 coins to pass the level.
# The following APIs are available on your team's peasants: "snakeBackward"
# The following APIs are available on neutral peasants: "snakeBackward", "snakeHead", "snakeForward"
def moveTo(position, fast=True):
    if (self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)


# pickup coin
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def commandPeasant(peasant):
    item = peasant.findNearestItem()
    goalf = peasant.pos
    if item:
        vectorToH = Vector.subtract(item.pos, goalf)
        vectorToH = Vector.normalize(vectorToH)
        vectorToH = Vector.multiply(vectorToH, 10)
        goalf = Vector.add(goalf, vectorToH)
    enemies = peasant.findEnemies()
    for enemy in enemies:
        if peasant.distanceTo(enemy) < 5:
            vectorToH = Vector.subtract(friend.pos, enemy.pos)
            vectorToH = Vector.normalize(vectorToH)
            vectorToH = Vector.multiply(vectorToH, 5)
            goalf = Vector.add(vectorToH, goalf)
    self.command(peasant, 'move', goalf)


def CommandArcher(soldier):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(soldier, "attack", target)


summonTypes = ['peasant']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


loop:
friends = self.findFriends()
summonTroops()
tails = self.findEnemies()
coins = self.findItems()
# pickUpNearestItem(coins)
for friend in friends:
    if friend.type == 'archer':
        CommandArcher(friend)
    elif friend.type == 'peasant':
        commandPeasant(friend)
