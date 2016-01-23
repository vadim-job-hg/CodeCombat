step = 0
def choiseTarget(enemies):
    self.say(enemies)
    for enemy in enemies:
        for att in attack:
            if att[0] == enemy.pos.x and att[1] == enemy.pos.y:
                return enemy
    return None
def сommandTroops():    
    for index, friend in enumerate(self.findFriends()):
        if (step==0 and friend.pos.y>60 and (friend.type != 'archer' or self.now()>3.7)):
            enemy = friend.findNearestEnemy()
            if enemy:  
                self.command(friend, "attack", enemy) 
        elif friend.type == 'archer':
            CommandArcher(friend)        
        elif friend.type == 'paladin':
            CommandPaladin(friend)   
        else:
            CommandSoldier(friend)
def CommandPaladin(soldier):
    if(soldier.canCast("heal") and self.now()>3):
        self.command(soldier, "cast", "heal", soldier)  
    elif self.now()>3 and soldier.health<soldier.maxHealth*0.7:        
        self.command(soldier, "shield")
    pass
def CommandSoldier(soldier):
   if step==1:
        enemy = soldier.findNearestEnemy()
        if enemy:  
            self.command(soldier, "attack", enemy) 

def CommandArcher(soldier):       
    if step == 1:   
        self.command(soldier, "move", {'x':22, 'y':55})
def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)
index = 0
route = [[33, 12, False], [34, 9, False], [32, 6, False], [32, 14, False]]
def moveHero():
    if len(route)>index:
        moveTo({'x':route[index][0],'y':route[index][1]}, route[index][2])
        if(self.pos.x==route[index][0] and self.pos.y==route[index][1]):
            return True
        else:
            return False    
loop:
    if(self.now()>6 and self.now()<600):
        step = 1
    сommandTroops()    
    if moveHero():
        index = index + 1    
        
