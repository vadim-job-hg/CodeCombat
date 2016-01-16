def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)

summonTypes = ['griffin-rider','soldier', 'archer']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)
        
def commandTroops():
    for soldier in self.findFriends():
        if enemy:
             self.command(soldier, "attack", enemy)

def attack(target):
       if(self.distanceTo(target)>10):
            moveTo(target.pos)        
        else:
            self.attack(target)

loop:
    summonTroops()
    commandTroops()
    enemy = self.findNearest(self.findEnemies())
    if(enemy):
        attack(enemy)
