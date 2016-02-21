# http://codecombat.com/play/level/serpent-savings
# You cannot collect coins.
# Summon peasants to collect coins for you.
# Collecting coins spawns a growing 'tail' behind the peasants.
# When a peasant touches a tail, they die.
# Collect 500 coins to pass the level.
# The following APIs are available on your team's peasants: "snakeBackward"
# The following APIs are available on neutral peasants: "snakeBackward", "snakeHead", "snakeForward"
def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)

#pickup coin
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)
        
def commandPeasant(peasant):
    item = peasant.findNearestItem()
    goalf = item.pos
    #if item:
    #    goalf = Vector.subtract(goalf, item.pos)
    #    goalf = Vector.normalize(goalf)
    #    goalf = Vector.multiply(goalf, 10)
    enemies = peasant.findEnemies()
    #for enemy in enemies:
    #    if peasant.distanceTo(enemy)<10:
    #        vectorToH = Vector.subtract(friend.pos, enemy.pos)
    #        vectorToH = Vector.normalize(vectorToH)
    #        vectorToH = Vector.multiply(vectorToH, 10)
    #       goalf =  Vector.add(vectorToH, goalf)            
    self.command(peasant, 'move', goalf)
       
def CommandArcher(soldier):
    target = self.findNearest(self.findEnemies())
    if target:
        self.command(soldier, "attack", target)       
        
summonTypes = ['peasant', 'archer', 'archer', 'archer','archer']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)

loop:    
    friends = self.findFriends()
    #summonTroops()
    tails = self.findEnemies()
    coins = self.findItems()
    #pickUpNearestItem(coins)
    for friend in friends:
        if friend.type == 'archer':
            CommandArcher(friend)
        elif friend.type == 'peasant':
            commandPeasant(friend)
