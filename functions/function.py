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

def findTheY(x1, x2, y1, y2, x):
    if(y2!=y1):
        y = (x - x1)/(x2 - x1)*(y2 - y1) + y1
    else:
        y = y1
    return y

def findTheMiddle(pos1, pos2):
    return {'x':(pos1.x+pos2.x)/2,'y':(pos1.y+pos2.y)/2}

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