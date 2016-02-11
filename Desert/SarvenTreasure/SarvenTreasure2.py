def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)

def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)
        
def attack(target):
    if target:
        if(self.distanceTo(target)<10 and self.isReady("bash")):
            self.bash(target)
index = 0            
route = [[7, 19, True, [5, 20]], [75, 19, True, [77, 20]]]
def moveHero():
    ind = index%len(route)
    moveTo({'x':route[ind][0],'y':route[ind][1]}, route[ind][2])
    if(self.pos.x==route[ind][0] and self.pos.y==route[ind][1]):
        #self.say(route[ind][3]);
        self.moveXY(route[ind][3][0], route[ind][3][1])
        return True
    else:
        return False
loop:
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    items = self.findItems()
    item = self.findNearest(items)
    if enemy and self.distanceTo(enemy)>10 and items and (item.pos.x<30 or item.pos.x>60):
        pickUpNearestItem(items)
    #elif(enemy and self.isReady("bash")):
    #    self.bash(enemy)
    #elif(enemy and self.canCast('chain-lightning', enemy)):
    #    self.cast('chain-lightning', enemy)
    elif(moveHero()):
        index = index + 1
