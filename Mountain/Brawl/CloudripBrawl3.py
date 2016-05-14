enemy_types = {}
enemy_types['shaman'] = {'danger':10, 'focus':50}
enemy_types['warlock'] = {'danger':10, 'focus':30}
enemy_types['arrow-tower'] = {'danger':10, 'focus':20}
enemy_types['catapult'] = {'danger':10, 'focus':100}
enemy_types['artillery'] = {'danger':10, 'focus':100}
enemy_types['witch'] = {'danger':8, 'focus':50}
enemy_types['brawler'] = {'danger':7, 'focus':55}
enemy_types['ogre'] = {'danger':5, 'focus':40}
enemy_types['chieftain'] = {'danger':6, 'focus':35}
enemy_types['fangrider'] = {'danger':4, 'focus':22}
enemy_types['skeleton'] = {'danger':5, 'focus':22}
enemy_types['thrower'] = {'danger':3, 'focus':22}
enemy_types['munchkin'] = {'danger':2, 'focus':15}
enemy_types['yak'] = {'danger':-1, 'focus':0}
enemy_types['ice-yak'] = {'danger':-1, 'focus':0}
def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger>danger:
            enemy =  self.findNearest(self.findByType(type))
            if enemy and self.distanceTo(enemy)<enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    return enemy_return

def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)
        
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
        elif(self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        elif(self.isReady("attack")):
            self.attack(target)
        else:
            self.shield()
       
summonTypes = ['paladin']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)
        
def сommandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)        
        elif friend.type == 'paladin':
            CommandPaladin(friend)   
        elif friend.type == 'soldier':
            CommandSoldier(friend)
            
def CommandPaladin(paladin):
    if(paladin.canCast("heal") and self.health<self.maxHealth*0.6):
        self.command(paladin, "cast", "heal", hero)
    else:
        if enemyattack:
            self.command(paladin, "defend", hero)

def CommandSoldier(soldier):
    if enemyattack:
        self.command(soldier, "defend", hero)

def CommandArcher(soldier):
    if enemyattack:
        self.command(soldier, "defend", hero)



def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend
loop:
    if(self.canCast('invisibility', self)):
        self.cast('invisibility', self)
    summonTroops()
    сommandTroops()
    items = self.findItems()
    enimies = self.findEnemies()
    enemy = self.findNearest(enimies)
    enemyattack = findTarget()
    if(len(items)>0):
        pickUpNearestItem(items)
    
