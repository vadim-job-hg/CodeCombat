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


redX = {"x": 28, "y": 36}
whiteX = {"x": 44, "y": 36}

# Выбери цвет.
self.setFlowerColor("red") 
# Нарисуй круг размером 10 на красной метке.
drawCircle(redX.x, redX.y, 10)
# Измени цвет!
self.setFlowerColor("white") 
# Нарисуй квадрат размером 10 на белой метке.
drawSquare(whiteX.x, whiteX.y, 10)
# Теперь экспериментируй, рисуя все что угодно!
size = 10
self.setFlowerColor("random") 
self.toggleFlowers(False)
cornerOffset = size / 2
self.moveXY(59, 37)
self.toggleFlowers(True)
x = 60
y = 26
angle = 0
while angle <= Math.PI * 2:
    newX = x + (size * Math.cos(angle))
    newY = y + (size * Math.sin(angle))
    self.moveXY(newX, newY)
    self.toggleFlowers(True)
    angle += 0.2
x = 60
y = 46
angle = 0
while angle <= Math.PI * 2:
    newX = x + (size * Math.cos(angle))
    newY = y + (size * Math.sin(angle))
    self.moveXY(newX, newY)
    self.toggleFlowers(True)
    angle += 0.2
