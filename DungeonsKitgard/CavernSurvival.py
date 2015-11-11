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
        enemy = self.findNearest(self.findEnemies())
        if enemy:
             self.command(soldier, "attack", enemy)

def attack(target):
        if(not target or self.distanceTo(target)>20):
            self.buildXY('caltrops', self.pos.x, self.pos.y)
        elif(self.distanceTo(target)>10):
            moveTo(target.pos)        
        else:
            self.attack(target)

loop:
    summonTroops()
    commandTroops()
    attack(self.findNearest(self.findEnemies()))
