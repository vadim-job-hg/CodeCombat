def pickUpNearestCoin():
    items = self.findItems()
    nearestCoin = self.findNearest(items)
    if nearestCoin:
        self.move(nearestCoin.pos)

def attack(target):
    if target:
        if(self.isReady("jump") and self.distanceTo>10):
            self.jumpTo(enemy.pos)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif(self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.attack(enemy)
            
summonTypes = ['griffin-rider', 'soldier', 'archer']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)

# commands attack
def commandSoldiers():
    for soldier in self.findByType("soldier"):
        self.command(soldier, "defend", self)
            
loop:
    enemies = self.findEnemies()
    index = 0
    distanse = 99999
    enemy = None
    while index<len(enemies):
        if enemies[index].type != "sand-yak" and distanse>self.distanceTo(enemies[index]):
            distanse = self.distanceTo(enemies[index])
            enemy = enemies[index]
        index +=1
    items  = self.findItems()
    if len(items)>0:
        pickUpNearestCoin()
    if enemy is not None and enemy.type != "sand-yak":
        if(self.distanceTo(enemy)<7):
            attack(enemy)        
        elif(self.distanceTo(enemy)<20):
            if(self.isReady("jump") and self.distanceTo>10):
                self.jumpTo(enemy.pos)
            else:
                self.move(enemy.pos)
        else:
            self.move({'x':89, 'y':72})
    summonTroops()
    commandSoldiers()
        
        
