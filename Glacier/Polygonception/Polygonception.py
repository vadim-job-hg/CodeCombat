# https://codecombat.com/play/level/polygonception
# Теперь ты сам по себе, и я надеюсь, что на предыдущих уровнях ты узнал достаточно о фрактальных многоугольниках.

# Тебе нужна функция для перевода градусов в радианы. Умножь градусы на `Math.PI / 180`.
def degreesToRadians(degrees):
    # Все векторные операции предпочтительнее выполнять в радианах, нежели в градусах.
    return Math.PI / 180 * degrees


# Твоя функция полигона должна принимать 3 параметра: начало, конец, число сторон.
def polygon(start_, end_, side):
    start = start_
    end = end_
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    # Если ниже порогового размера, то просто построим линию вдоль вектора и закончим (возврат из функции).
    hero.toggleFlowers(False)
    hero.moveXY(start.x, start.y)
    hero.toggleFlowers(True)
    for i in range(side):
        hero.moveXY(end.x, end.y)
        full = Vector.rotate(full, degreesToRadians(360 / side))
        if distance > 10:
            polygon(end, Vector.add(end, Vector.divide(full, 5)), side)
        end = Vector.add(end, full)


        # Помни, что нужно сделать полигон рекурсивным, нарисовав дополнительные фигуры на каждом углу.


# Чтобы получить начальную и конечную позиции для полигона, добавь `startOffset` и `endOffset` к позиции яка.
startOffset = Vector(-15, -15)
endOffset = Vector(15, -15)

# Ты должен перебрать яков, нарисовав многоугольник вокруг каждого.
startOffset = Vector(-15, -15)
endOffset = Vector(15, -15)
enemies = self.findEnemies()
for enemy in enemies:
    start = Vector.add(enemy.pos, startOffset)
    end = Vector.add(enemy.pos, endOffset)
    sides = enemy.sides
    polygon(start, end, sides)
