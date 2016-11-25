def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend


def commandPeasant(peasant):
    item = peasant.findNearestItem()
    if item:
        hero.command(peasant, 'move', item.pos)


def commandPaladin(paladin):
    if (paladin.canCast("heal")):
        target = lowestHealthPaladin()
        if target:
            hero.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        hero.command(paladin, "shield")
    else:
        target = paladin.findNearestEnemy()
        if (target):
            hero.command(paladin, "attack", target)


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


def findTheY(x1, x2, y1, y2, x):
    if (y2 != y1):
        y = (x - x1) / (x2 - x1) * (y2 - y1) + y1
    else:
        y = y1
    return y


def findTheMiddle(pos1, pos2):
    return {'x': (pos1.x + pos2.x) / 2, 'y': (pos1.y + pos2.y) / 2}

def aroundMine1(move, trap, radius = 3):
    way = Vector.subtract(hero.pos, trap.pos)
    normal = Vector.normalize(way)
    direction = Vector.multiply(normal, radius+1)
    wayCorr =  Vector.add(trap.pos, direction)
    dot = Vector.normalize(move)
    dot = Vector.add(wayCorr, dot)
    way = Vector.subtract(dot, trap.pos)
    normal = Vector.normalize(way)
    direction = Vector.multiply(normal, radius+1)
    wayCorr =  Vector.add(trap.pos, direction)
    return wayCorr