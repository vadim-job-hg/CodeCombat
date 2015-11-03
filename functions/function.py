#pickup coin
def pickUpNearestCoin():
    items = self.findItems()
    nearestCoin = self.findNearest(items)
    if nearestCoin:
        self.move(nearestCoin.pos)

# add soldier
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")


# commands attack
def commandSoldiers():
    for soldier in self.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            self.command(soldier, "attack", enemy)

def attack(target):
    if target:
        if(self.isReady("jump") and self.distanceTo>10):
            self.jumpTo(enemy.pos)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif(self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.attack(enemy)

def tacktick():
    enemies = self.findEnemies()
    nearest = self.findNearest(enemies)
    friends = self.findFriends()
    if self.distanceTo(nearest)<10:
        attack(nearest)
    elif len(friends)/3<len(enemies):
        attack(nearest)
    else:
        pickUpNearestCoin()

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

