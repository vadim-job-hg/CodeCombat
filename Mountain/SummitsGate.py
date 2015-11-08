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
     target = self.findNearest(self.findEnemies()) 
     if(target):
        self.command(soldier, "attack", target)

def commandArcher(soldier):
     if(len(self.findByType('ogre'))>0):
        target = self.findNearest(self.findByType('ogre'))
     else:
        target = self.findNearest(self.findEnemies())
     if(target):
        self.command(soldier, "attack", target)

def commandElse(soldier):      
     if self.findNearest(self.findByType('catapult')):
         target = self.findNearest(self.findByType('catapult'))
     elif(len(self.findByType('ogre'))>0):
        target = self.findNearest(self.findByType('ogre'))
     else:
        target = self.findNearest(self.findEnemies())
     if(target):
        self.command(soldier, "attack", target)
        
def commandSlize(soldier, missiles):
    pass
    
def commandFriends():
    friends = self.findFriends()
    for friend in friends: 
        if self.now()<15:            
            self.command(friend, "defend", {'x':6, 'y':38})
        elif(self.now()<60 and self.now()>40):            
            self.command(friend, "defend", self)
        elif friend.type == "paladin":
            commandPaladin(friend)
        elif friend.type == "soldier":
            commandSoldier(friend)
        elif friend.type == "archer":
            commandArcher(friend)
        else:
            commandElse(friend)
            
def moveTo(position, fast = True):
    if(self.isReady("jump")):
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
            
def pickUpNearestItem():
    nearestItem = self.findNearest(self.findItems())
    if nearestItem:
        moveTo(nearestItem.pos)
        
loop:
    commandFriends()
    summonTroops()
    target = self.findNearest(self.findByType('catapult'))
    nearestItem = self.findNearest(self.findItems())
    if self.distanceTo(nearestItem)<30:
        pickUpNearestItem()
    elif target:
        attack(target)
    else:
        attack(self.findNearest(self.findEnemies()))
