def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)

summonTypes = ['griffin-rider','soldier', 'archer']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)
        
def commandTroops():
    for soldier in self.findFriends():
        enemy = self.findNearest(self.findEnemies())
        if enemy:
             self.command(soldier, "attack", enemy)
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)
        
def attack(target):
    if target:
        if(self.distanceTo(target)<10 and self.isReady("bash")):
            self.bash(target)
            
buildTypes = ["fire-trap"]
def buildTroops():
    enemy = self.findNearest(self.findEnemies())
    if enemy and self.distanceTo(enemy)<20:
        type = buildTypes[len(self.built)%len(buildTypes)]
        if self.gold > self.costOf(type):
            self.buildXY(type, enemy.pos.x, enemy.pos.y)
        
loop:
    items = self.findItems()
    if len(items)>0 and self.health < self.maxHealth*0.4:
        pickUpNearestItem(items)
    else:
        attack(self.findNearest(self.findEnemies()))
    buildTroops()
