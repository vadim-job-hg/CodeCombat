# Practice using modulo to loop over an array

# Choose the mix and order of units you want to summon by populating this array:
summonTypes = ['archer', 'archer', 'archer', 'archer', 'archer', 'archer', 'soldier']

def moveTo(position, fast = True):
    if(self.isReady("jump") and self.distanceTo>10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)

#pickup coin
def pickUpNearestItem():
    items =  self.findItems()
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)

def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)
        
def commandSoldiers():
    for soldier in self.findFriends():
        enemy = self.findNearest(self.findEnemies())
        if enemy and (soldier.type =='archer'  or soldier.type =='soldier'):
             self.command(soldier, "attack", enemy)
def attack(target):
    if target:
        if(self.distanceTo(target)>10):
            moveTo(target.pos)
        elif(self.isReady("bash")):
            self.bash(target)
        elif(self.isReady("attack")):
            self.attack(target)
        else:
            self.shield()             
loop:
    summonTroops()
    commandSoldiers()
    enemy = self.findNearest(self.findEnemies())
    if(enemy and self.distanceTo(enemy)<10):
        attack(enemy)
    else:
        pickUpNearestItem()
