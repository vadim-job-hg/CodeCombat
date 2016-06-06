#http://codecombat.com/play/level/kelvintaph-defiler
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
        elif step == 4:
            self.command(friend, "move", {'x':42, 'y':67})
        elif friend.type == 'archer':
            CommandArcher(friend)        
        elif friend.type == 'paladin':
            CommandPaladin(friend)   
        else:
            CommandSoldier(friend)
def CommandPaladin(soldier):
    if step <4:
        if(soldier.canCast("heal") and self.now()>3):
            self.command(soldier, "cast", "heal", soldier)  
        elif self.now()>3 and soldier.health<soldier.maxHealth*0.7:        
            self.command(soldier, "shield")

def CommandSoldier(soldier):
   if step<4:
        if soldier.pos.x<74:
            self.command(soldier, "move", {'x':76, 'y':76})
        else:
            enemy = soldier.findNearestEnemy()
            if enemy:  
                self.command(soldier, "attack", enemy) 

def CommandArcher(soldier):       
    if step == 1:
        if soldier.pos.y>60:
            self.command(soldier, "move", {'x':22, 'y':55})
        else:
            enemies = soldier.findEnemies()
            for enemy in enemies:
                if enemy.type != 'yeti':
                    self.command(soldier, "attack", enemy)
    elif step ==2:
        if soldier.pos.x>14:
            self.command(soldier, "move", {'x':8, 'y':77})
        else:
            enemy = soldier.findNearestEnemy()
            if enemy:  
                self.command(soldier, "attack", enemy)
     elif step ==3:           
        if soldier.pos.x<74:
            self.command(soldier, "move", {'x':76, 'y':76})
        else:
            enemy = soldier.findNearestEnemy()
            if enemy:  
                self.command(soldier, "attack", enemy)
        
def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)
index = 0
route = [[33, 12, False], [34, 9, False], [32, 6, False]]
def moveHero():
    if len(route)>index:
        moveTo({'x':route[index][0],'y':route[index][1]}, route[index][2])
        if(self.pos.x==route[index][0] and self.pos.y==route[index][1]):
            return True
        else:
            return False    
def attack(target):
    if target:
        if(self.distanceTo(target)>10):
            moveTo(target.pos)
        elif(self.isReady("bash")):
            self.bash(target)        
        else:
            self.attack(target)
loop:
    if(self.now()>6 and self.now()<12):
        step = 1
    elif(self.now()>10 and self.now()<17):
        step = 2
    elif(self.now()>15 and self.now()<30):
        step = 3
    elif(self.now()>28 and self.now()<600):
        step = 4
    сommandTroops() 
    if step<4:
        if moveHero():
            index = index + 1   
    else:
        enemy = self.findNearest(self.findEnemies())
        if enemy:
            attack(enemy)
        else:
            moveTo({'x':74, 'y':44})
        

        
