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

# add soldier
buildTypes = ['arrow-tower']
def buildTroops():
    type = buildTypes[len(self.built)%len(buildTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)
# commands attack
#def commandTroops():
#    for soldier in self.findFriends():
#        enemy = self.findNearest(self.findEnemies())
#        if enemy:
#             self.command(soldier, "attack", enemy)
