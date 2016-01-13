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

# add soldier
summonTypes = ['griffin-rider','soldier', 'archer']
def summonTroops():
    type = summonTypes[len(self.built)%len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)
#build
coors = [[67, 41], [24, 54], [69, 55], [25,  34], [69, 32]]
buildTypes = ["fire-trap", "decoy", "arrow-tower"]
def buildTroops():
    coor = coors[len(self.built)%len(coors)]
    type = buildTypes[len(self.built)%len(buildTypes)]
    if self.gold > self.costOf(type):
        self.buildXY(type, coor[0], coor[1])

# commands attack
def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        enemy = self.findNearest(self.findEnemies())
        if enemy:
             self.command(friend, "attack", enemy)

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
        else:
            self.attack(target)

def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend

def commandPeasant(peasant):
   item = peasant.findNearestItem()
   if item:
       self.command(peasant, 'move', item.pos)

def commandPaladin(paladin):
    if(paladin.canCast ("heal")):
        target = lowestHealthPaladin()
        if target:
            self.command(paladin, "cast", "heal", target)
    elif(paladin.health<100):
        self.command(paladin, "shield")
    else:
        target = paladin.findNearestEnemy()
        if(target):
            self.command(paladin, "attack", target)
# Теперь у тебя есть Кольца Цветов! Ты можешь:
# toggleFlowers(true/false) - включить или выключить.
# setFlowerColor("random") - также можно выбрать "pink", "red", "blue", "purple", "yellow", или "white".
# Вот некоторые функции для рисования фигур:
# х, у - центр фигуры
# size - размер фигуры (radius, side length)
def drawCircle(x, y, size):
    angle = 0
    self.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        self.moveXY(newX, newY)
        self.toggleFlowers(True)
        angle += 0.2

def drawSquare(x, y, size):
    self.toggleFlowers(False)
    cornerOffset = size / 2
    self.moveXY(x - cornerOffset, y - cornerOffset)
    self.toggleFlowers(True)
    self.moveXY(x + cornerOffset, y - cornerOffset)
    self.moveXY(x + cornerOffset, y + cornerOffset)
    self.moveXY(x - cornerOffset, y + cornerOffset)
    self.moveXY(x - cornerOffset, y - cornerOffset)

