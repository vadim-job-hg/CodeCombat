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
   if item:
       self.command(peasant, 'move', item.pos)
       
summonTypes = ['peasant']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)

loop:
    summonTroops()
    friends = self.findFriends()
    tails = self.findEnemies()
    coins = self.findItems()
    pickUpNearestItem(coins)
    for friend in friends:
        if friend.type == 'peasant':
            CommandPeasant(friend)
