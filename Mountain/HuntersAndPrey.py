# http://codecombat.com/play/level/hunters-and-prey

def pickUpCoin():
    items = self.findItems()
    nearestCoin = self.findNearest(items)
    if nearestCoin:
        self.move(nearestCoin.pos)

def summonTroops():
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")
    
# This function has an argument named soldier.
# Arguments are like variables.
# The value of an argument is determined when the function is called.
def commandSoldier(soldier):
    enemy = soldier.findNearestEnemy()
    if enemy:
        self.command(soldier, "attack", enemy)

# Write a commandArcher function to tell your archers what to do!
# It should take one argument that will represent the archer passed to the function when it's called.
# Archers should only attack enemies who are closer than 25 meters, otherwise, stay still
def commandArcher(soldier):
    enemy = soldier.findNearestEnemy()
    if enemy and soldier.distanceTo(enemy)<25:
        self.command(soldier, "attack", enemy)

loop:
    pickUpCoin()
    summonTroops()
    friends = self.findFriends()
    for friend in friends:
        if friend.health<100 and (friend.type == "soldier"):
            self.command(friend, "defend", self.pos)
        elif friend.type == "soldier":
            # This friend will be assigned to the variable soldier in commandSoldier
            commandSoldier(friend)
        elif friend.type == "archer":
            commandArcher(friend)

