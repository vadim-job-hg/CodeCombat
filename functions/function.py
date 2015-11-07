def moveTo(position, fast = True):
    if(self.isReady("jump") and self.distanceTo>10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)

#pickup coin
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem:
        moveTo(items.pos)

# add soldier
list = ['soldier']
indexSoldier = 1
def summonSoldier():
    if self.gold > self.costOf(list[indexSoldier%len(list)]):
        self.summon(list[indexSoldier%len(list)])
        indexSoldier +=1

# commands attack
def commandSoldiers():
    for soldier in self.findFriends():
        enemy = self.findNearest(self.findEnemies())
        if enemy:
             self.command(soldier, "attack", enemy)

def attack(target):
    if target:
        if(self.distanceTo(target)>10):
            moveTo(enemy.pos)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif(self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.attack(enemy)

def commandSoldiers2():
    for soldier in self.findByType("soldier"):
        enemy = self.findNeares(self.findEnemies())
        if enemy:
             self.command(soldier, "attack", enemy)

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

