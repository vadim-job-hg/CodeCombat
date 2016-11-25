# Этот уровень - место рисования цветками.
# Цель - экспериментировать и получать удовольствие!
# Если ты что-либо нарисуешь, используя 1000 цветков, ты пройдешь уровень.
colors = ["pink", "red", "blue", "purple", "yellow", "white", "random"]
index = len(colors)


def drawCircle(x, y, size):
    angle = 0
    hero.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += 0.2


for i in range(30, 120, 30):
    for j in range(30, 120, 30):
        color = colors[index % len(colors)]
        hero.setFlowerColor(color)
        index += 1
        drawCircle(i, j, 10)
