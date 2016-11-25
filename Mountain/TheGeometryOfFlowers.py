# Теперь у тебя есть Кольца Цветов! Ты можешь:
# toggleFlowers(true/false) - включить или выключить.
# setFlowerColor("random") - также можно выбрать "pink", "red", "blue", "purple", "yellow", или "white".

# Вот некоторые функции для рисования фигур:
# х, у - центр фигуры
# size - размер фигуры (radius, side length)
def drawCircle(x, y, size):
    angle = 0
    hero.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += 0.2


def drawSquare(x, y, size):
    hero.toggleFlowers(False)
    cornerOffset = size / 2
    hero.moveXY(x - cornerOffset, y - cornerOffset)
    hero.toggleFlowers(True)
    hero.moveXY(x + cornerOffset, y - cornerOffset)
    hero.moveXY(x + cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y - cornerOffset)


redX = {"x": 28, "y": 36}
whiteX = {"x": 44, "y": 36}

# Выбери цвет.
hero.setFlowerColor("red")
# Нарисуй круг размером 10 на красной метке.
drawCircle(redX.x, redX.y, 10)
# Измени цвет!
hero.setFlowerColor("white")
# Нарисуй квадрат размером 10 на белой метке.
drawSquare(whiteX.x, whiteX.y, 10)
# Теперь экспериментируй, рисуя все что угодно!
size = 10
hero.setFlowerColor("random")
hero.toggleFlowers(False)
cornerOffset = size / 2
hero.moveXY(59, 37)
hero.toggleFlowers(True)
x = 60
y = 26
angle = 0
while angle <= Math.PI * 2:
    newX = x + (size * Math.cos(angle))
    newY = y + (size * Math.sin(angle))
    hero.moveXY(newX, newY)
    hero.toggleFlowers(True)
    angle += 0.2
x = 60
y = 46
angle = 0
while angle <= Math.PI * 2:
    newX = x + (size * Math.cos(angle))
    newY = y + (size * Math.sin(angle))
    hero.moveXY(newX, newY)
    hero.toggleFlowers(True)
    angle += 0.2
