attack = [42, 62]
aInd = 0
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
        if friend.type == 'archer':
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
    if self.now()<7.6:
        self.command(soldier, "move", {'x':75, 'y':75})
    elif self.now()<15:
         enemies = soldier.findEnemies()
         for enemy in enemies:
            if enemy and enemy.pos.x>36:
                self.command(soldier, "attack", enemy)
                break    
    else:
        enemy = soldier.findNearestEnemy()
        if enemy:  
            self.command(soldier, "attack", enemy)

def CommandArcher(soldier):
        enemies = soldier.findEnemies()
        if ((self.now()>2.5 or soldier.pos.x>20) and (self.now()<10)):
            for enemy in enemies:
                if enemy and (enemy.type=='yeti' and enemy.health>99):
                    self.command(soldier, "attack", enemy)
                    break      
        elif(self.now()<60 and self.now()>=10):
            if self.pos.y>21:
                enemy = soldier.findNearestEnemy();
                if enemy:
                    self.command(soldier, "attack", enemy)
                else:
                    self.command(soldier, "move", {'x':21, 'y':67})  
                
        
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
    сommandTroops()    
    if moveHero():
        index = index + 1
