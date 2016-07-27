colors = ["pink", "red", "blue", "purple", "yellow", "white", "random"]
index = len(colors)


def drawCircle(x, y, size):
    angle = 0
    self.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        self.moveXY(newX, newY)
        self.toggleFlowers(True)
        angle += 0.2


for i in range(30, 120, 10):
    for j in range(30, 120, 10):
        color = colors[index % len(colors)]
        self.setFlowerColor(color)
        index += 1
        drawCircle(i, j, 5)
