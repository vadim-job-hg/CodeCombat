enemy_types = {}
enemy_types['door'] = {'danger':1000, 'focus':200}
enemy_types['knight'] = {'danger':100, 'focus':100}
enemy_types['potion-master'] = {'danger':100, 'focus':100}
enemy_types['ranger'] = {'danger':100, 'focus':100}
enemy_types['trapper'] = {'danger':100, 'focus':100}
enemy_types['samurai'] = {'danger':100, 'focus':100}
enemy_types['librarian'] = {'danger':100, 'focus':100}
enemy_types['sorcerer'] = {'danger':100, 'focus':100} 
enemy_types['hero-placeholder-1'] = {'danger':99, 'focus':100}
enemy_types['hero-placeholder-2'] = {'danger':99, 'focus':100}
enemy_types['burl'] = {'danger':10, 'focus':20}
enemy_types['necromancer'] = {'danger':100, 'focus':100}
enemy_types['captain'] = {'danger':100, 'focus':100} 
enemy_types['shaman'] = {'danger':10, 'focus':50} 
enemy_types['warlock'] = {'danger':10, 'focus':30}
enemy_types['arrow-tower'] = {'danger':10, 'focus':20}
enemy_types['catapult'] = {'danger':10, 'focus':100}
enemy_types['artillery'] = {'danger':10, 'focus':100} 
enemy_types['witch'] = {'danger':8, 'focus':50}
enemy_types['brawler'] = {'danger':7, 'focus':55}
enemy_types['ogre'] = {'danger':5, 'focus':40}
enemy_types['chieftain'] = {'danger':6, 'focus':35}
enemy_types['thrower'] = {'danger':3, 'focus':22}
enemy_types['fangrider'] = {'danger':4, 'focus':22}
enemy_types['munchkin'] = {'danger':2, 'focus':15}
enemy_types['yak'] = {'danger':-1, 'focus':0}
enemy_types['ice-yak'] = {'danger':-1, 'focus':0}
def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger>danger:
            enemy =  self.findNearest(self.findByType(type))
            if enemy and self.distanceTo(enemy)<enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if enemy_return is None:
        enemy_return =  self.findNearest(self.findEnemies())
    return enemy_return

def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)
        
def moveTo(position, fast = True):    
    if(self.isReady("jump") and self.distanceTo(position)>10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)
        
def attack(target):
    if target:
        if(self.canCast('invisibility', self)):
            self.cast('invisibility', self)
        elif self.hasEffect('invisibility'):
            moveTo(target.pos)
        else:
            if(self.canCast('earthskin', self)):
                self.say('cast');
                self.cast('earthskin', self)
            elif(self.distanceTo(target)>10):
                moveTo(target.pos)
            elif(self.isReady("bash")):
                self.bash(target)
            elif(self.canCast('chain-lightning', target)):
                self.cast('chain-lightning', target)
            elif(self.isReady("attack")):
                self.attack(target)
            else:
                self.shield()
       
summonTypes = ['paladin','paladin','paladin','paladin']
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
        elif friend.type == 'peasant':
            CommandPeasant(friend)
            
def CommandPaladin(paladin):
    if(paladin.canCast ("heal") and self.health<self.maxHealth*0.6):
        self.command(paladin, "cast", "heal", self)
    else:
        enemyattack = findTarget()
        if enemyattack:
            self.command(paladin, "attack", enemyattack)
        else:
            self.command(paladin, "defend", self)

def CommandSoldier(soldier):
    pass

def CommandArcher(soldier):
    if enemyattack:
        self.command(soldier, "attack", enemyattack)

def CommandPeasant(soldier):
    if enemyattack:
        self.command(soldier, "attack", enemyattack)

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
    items = self.findItems()
    enimies = self.findEnemies()
    #for enemy in enimies:
     #   self.say(enemy.type)
    if(len(items)>0 and self.health<self.maxHealth*0.5):
        pickUpNearestItem(items)
    else:            
        enemyattack = findTarget()
        if not enemyattack:
            enemyattack = self.findNearest(self.findEnemies())
        if(enemyattack):       
            attack(enemyattack)
        else:
            self.shield() 
    if self.health<self.maxHealth*0.6:
        summonTroops()
    
    сommandTroops()
