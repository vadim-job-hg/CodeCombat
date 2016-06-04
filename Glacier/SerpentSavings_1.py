# You cannot collect coins.
distance = 5
def getDirrection(diffy, diffx):    
    if(Math.abs(diffy)>1):
        if diffy>0:
           return Vector(0, distance)
        else:
           return Vector(0, -distance)
    else:
        if diffx>0:
            return Vector(distance, 0)
        else:
            return Vector(-distance, 0)
            
def commandPeasant(peasant, enemies):
    wait = False
    item = peasant.findNearestItem()   
    diffy = item.pos.y-peasant.pos.y
    diffx = item.pos.x-peasant.pos.x
    way = getDirrection(diffy, diffx)    
    for enemy in enemies:
        if peasant.distanceTo(enemy)<2:
            diffy = peasant.pos.y - enemy.pos.y
            diffx = peasant.pos.x - enemy.pos.x
            way = getDirrection(diffy, diffx)
            wait = True
    direction = Vector.add(way, peasant.pos)
    self.command(peasant, 'move', direction)


        
summonTypes = ['peasant']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)

loop:    
    enemies = self.findEnemies()
    friends = self.findFriends()
    for friend in friends:        
        commandPeasant(friend, enemies)
