#http://codecombat.com/play/level/brewball?session=56c5ebfded946a44004fb659&observing=true
#http://codecombat.com/play/level/brewball?session=56c5ebfded946a44004fb659&observing=true
# Скажи кое-что в расстоянии 10м от Омарна чтобы он кинул зелье.
# Поймай зелье стоя рядом с ним прежде чем он упадет.
# НЕ ДАЙ ЗЕЛЬЮ УПАСТЬ НА ЗЕМЛЮ!
def mineGo(trap, go):

    pass
while True:
    potion = hero.findFriendlyMissiles()[0]
    firetraps = hero.findHazards()
    start = Vector(9, 34)
    # Запомни что огненная ловушка сработает если ты подойдешь ближе чем 3 метра!
    omarn = hero.findByType("potion-master")[0]
    if potion:
        dest = potion.targetPos
        go = self.pos
        add = Vector.subtract(potion.pos, go)
        add = Vector.normalize(add)
        add = Vector.multiply(add, 1)
        go = Vector.add(add, go)
        trap = self.findNearest(firetraps)
        if trap and self.distanceTo(trap)<6:
            go = mineGo(trap, go)
        self.move(go)
    else:
        if omarn and hero.distanceTo(omarn) > 10:
            # Вернись к Омарну.
            go = self.pos
            add = Vector(14, 34)
            add = Vector.subtract(go, add)
            add = Vector.normalize(add)
            add = Vector.multiply(add, 1)
            go = Vector.add(add, go)
            trap = self.findNearest(firetraps)
            if trap and self.distanceTo(trap)<4:
                vector = Vector.subtract(self.pos, trap.pos)
                vector = Vector.normalize(vector)
                vector = Vector.multiply(vector, 5)
            go = Vector.add(vector, go)
            self.move(go)
            # Предупреждение: isPathClear не работает с Радиацией!
            pass
        else:
            hero.say("Hup, hup!")
