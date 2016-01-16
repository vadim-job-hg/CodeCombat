#http://codecombat.com/play/level/dueling-grounds
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
        if target:
             self.command(soldier, "attack", target)

def attack(target):
        if(self.distanceTo(target)>10):
            moveTo(target.pos)
        elif(self.isReady("bash")):
            self.bash(target)
        else:
            self.attack(target)

loop:
    summonTroops()
    commandTroops()
    target = self.findNearest(self.findEnemies())
    knight = self.findNearest(self.findByType('knight'))
    captain = self.findNearest(self.findByType('captain'))
    #Enemies = self.findEnemies()
    #for en in Enemies:
        #self.say(en.type)
    if(knight and self.distanceTo(knight)<20):
        target = knight
    if(captain and self.distanceTo(captain)<20):
        target = captain
    attack(target)

