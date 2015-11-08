def moveTo(position, fast = True):
    if(self.isReady("jump") and self.distanceTo>10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)

def chooseStrategy():
    enemies = self.findEnemies()

    # If you can summon a griffin-rider, return "griffin-rider"
    if self.gold > self.costOf("griffin-rider"):
        self.summon("griffin-rider")
    # If there is a fangrider on your side of the mines, return "fight-back"
    fangrider = self.findByType("fangrider")
    if(len(fangrider)>0 and fangrider[0].pos.x<38):
        return "fight-back"
    else:
        return "collect-coins"

def commandAttack():
    # Command your griffin riders to attack ogres.
    pass
    
def pickUpCoin():
    nearestItem = self.findNearest(self.findItems())
    if nearestItem:
        moveTo(nearestItem.pos)
    
def heroAttack():
    target = self.findNearest(self.findByType("fangrider"))
    if target:
        if(self.distanceTo(target)<20):
            moveTo(target.pos)
        elif(self.isReady("bash")):
            self.bash(target)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(target)
        elif(self.isReady("cleave")):
            self.cleave(target)
        else:
            self.attack(target)
def commandTroops():
    for soldier in self.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
             self.command(soldier, "attack", enemy)
             
loop:
    commandAttack()
    commandTroops()
    strategy = chooseStrategy()
    if(strategy=="fight-back"):
        heroAttack()    
    else:
        pickUpCoin()
