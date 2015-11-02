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
            
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")


# commands attack
def commandSoldiers():
    for soldier in self.findByType("soldier"):
        enemy = self.findNearestEnemy()
        if enemy:
            self.command(soldier, "attack", enemy)
            
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
    summonSoldier()
    commandSoldiers()
        
        
