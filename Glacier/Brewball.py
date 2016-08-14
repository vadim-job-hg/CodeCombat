# http://codecombat.com/play/level/brewball
# Скажи кое-что в расстоянии 10м от Омарна чтобы он кинул зелье.
# Поймай зелье стоя рядом с ним прежде чем он упадет.
# НЕ ДАЙ ЗЕЛЬЮ УПАСТЬ НА ЗЕМЛЮ!
def arowndMine(move, trap, radius = 3):
    way = Vector.subtract(hero.pos, trap.pos)
    normal = Vector.normalize(way)
    direction = Vector.multiply(normal, radius+3)
    wayCorr =  Vector.add(trap.pos, direction)
    dot = Vector.normalize(move)
    dot = Vector.add(wayCorr, dot)
    way = Vector.subtract(dot, trap.pos)
    normal = Vector.normalize(way)
    direction = Vector.multiply(normal, radius+2)
    wayCorr =  Vector.add(trap.pos, direction)
    return wayCorr
home = Vector(14, 34)
while True:
    potion = hero.findFriendlyMissiles()[0]
    firetraps = hero.findHazards()
    # Запомни что огненная ловушка сработает если ты подойдешь ближе чем 3 метра!
    omarn = hero.findByType("potion-master")[0]
    if potion:
        dest = potion.targetPos;
        direction = Vector.multiply(Vector.normalize(Vector.subtract(dest, hero.pos)), 3)
        move = Vector.add(hero.pos, direction)
        trap = self.findNearest(firetraps)
        if trap and self.distanceTo(trap) < 4:
            move = arowndMine(move, trap)
        hero.move(move)
    else:
        if omarn and hero.distanceTo(omarn) > 10:
            # Вернись к Омарну.
            direction = Vector.multiply(Vector.normalize(Vector.subtract(home, hero.pos)), 10)
            move = Vector.add(hero.pos, direction)
            # Предупреждение: isPathClear не работает с Радиацией!
            trap = self.findNearest(firetraps)
            if trap and self.distanceTo(trap) < 4:
                move = arowndMine(move, trap)
            hero.move(move)
        else:
            hero.say("Hup, hup!")
