def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)

#pickup coin
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)

buildTypes = ["fire-trap", "decoy", "arrow-tower"]
def buildTroops():
    coor = coors[len(self.built)%len(coors)]
    type = buildTypes[len(self.built)%len(buildTypes)]
    if self.gold > self.costOf(type):
        self.buildXY(type, coor[0], coor[1])
        
route = [[33, 14, True], [34, 7, False]]
index = 0
def moveHero():
    if len(route)>index:
        moveTo({'x':route[index][0],'y':route[index][1]}, route[index][2])
        if(self.pos.x==route[index][0] and self.pos.y==route[index][1]):
            return True
        else:
            return False
if(moveHero()):
    index = index + 1

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
        elif(self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        else:
            self.attack(target)
            self.shield()
