summonTypes = ['griffin-rider']
move = [{'x':153, 'y':34},{'x':191, 'y':21},{'x':245, 'y':25},{'x':360, 'y':40}]
index = len(move)
tactick = 'hold'
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
        if(self.health<self.maxHealth*0.7):
            target = self
        else:
            target = lowestHealthPaladin()        
        if target:
            self.command(paladin, "cast", "heal", target)
    elif now>45 and now<60:
        self.command(paladin, "move", self.pos)
    elif(paladin.health<200):
        self.command(paladin, "shield")    
    else:
        target = self.findNearest(self.findEnemies())
        if(warlock):
            target = warlock
        if(target):
            self.command(paladin, "attack", target)


def commandSoldier(soldier):         
     target = self.findNearest(self.findEnemies())
     if(warlock):
            target = warlock
     if(target):
        self.command(soldier, "attack", target)

def commandFriends():
    friends = self.findFriends()
    for friend in friends: 
        if tactick == 'hold':            
            self.command(friend, "defend", {'x':1, 'y':40})
        elif(tactick == 'defend'):            
            self.command(friend, "defend", self.pos)
        elif friend.type == "paladin":
            commandPaladin(friend)
        else:
            commandSoldier(friend)
            
def moveTo(position):
    if(self.isReady("jump")):
        self.jumpTo(position)
    else:
        self.move(position)
def attack(target):
    if target:
        if(self.distanceTo(target)>10):
            moveTo(target.pos)        
        else:
            self.attack(target)
            
def pickUpNearestItem():
    nearestItem = self.findNearest(self.findItems())
    if nearestItem:
        moveTo(nearestItem.pos)
        
commandFriends()
self.moveXY(31, 56)
loop: 
    catapult = self.findNearest(self.findByType('catapult'))
    warlock = self.findNearest(self.findByType('warlock'))
    target = self.findNearest(self.findEnemies())
    nearestItem = self.findNearest(self.findItems())
    now = self.now()
    if nearestItem and self.distanceTo(nearestItem)<10:
        pickUpNearestItem()
        tactick = 'attack'
        summonTroops()
    elif catapult:
        attack(catapult)
        tactick = 'hold'
    elif self.now()<45:
        tactick = 'defend'
        commandFriends()
        moveTo({"x":82, "y":33})
    elif self.pos.x<150 and self.now()>90:
        tactick = 'attack'
        commandFriends()
        moveTo({"x":154, "y":34})
    elif target and target.type!='tower':
        if(warlock):
            target = warlock
            summonTroops()
            attack(target)
        elif target:
            attack(target)
        elif nearestItem and self.distanceTo(nearestItem)<30:
            pickUpNearestItem()
            tactick = 'defend'
            summonTroops()  
        else:
            attack(target)
        tactick = 'attack'
    else:
        tactick = 'deffend'
        if now<120:
            moveTo({"x":247, "y":34})
        else:
            attack(target)
            summonTroops()
            tactick = 'attack'
    commandFriends()
