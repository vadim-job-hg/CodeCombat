summonTypes = ['griffin-rider', 'soldier', 'archer']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)

def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend

def commandPaladin(paladin):
    if(paladin.canCast ("heal")):
        if(self.health<100):
            target = self
        else:
            target = lowestHealthPaladin()        
        if target:
            self.command(paladin, "cast", "heal", target)
    elif(paladin.health<200):
        self.command(paladin, "shield")
    else:
        if(len(self.findByType('catapult'))>0):
            target = self.findNearest(self.findByType('catapult'))
        else:
            target = self.findNearest(self.findEnemies())
        if(target):
            self.command(paladin, "attack", target)


def commandSoldier(soldier):
     if(len(self.findByType('catapult'))>0):
        target = self.findNearest(self.findByType('catapult'))
     else:              
        target = self.findNearest(self.findEnemies()) 
     if(target):
        self.command(soldier, "attack", target)
    
def commandFriends():
    friends = self.findFriends()
    for friend in friends:
        if friend.type == "paladin":
            commandPaladin(friend)
        else:
            commandSoldier(friend)
            
def moveTo(position, fast = True):
    if(self.isReady("jump") and self.distanceTo>10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)
def attack(target):
    if target:
        if(self.distanceTo(target)>10):
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
            
loop:
    commandFriends()
    summonTroops()
    attack(self.findNearest(self.findEnemies()))
