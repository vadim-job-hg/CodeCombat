# https://codecombat.com/play/level/snowflakes-on-the-ice?

# На этот уровне нам понадобится линейный фрактал, как основа для нашей шестиугольной снежинки. Сама снежинка будет состоять из 6 линейных фракталов. Обратись к описанию за инструкцией и изображением желаемого результата.
def degreesToRadians(degrees):
    # Все векторные операции предпочтительнее выполнять в радианах, нежели в градусах.
    return Math.PI / 180 * degrees


# Это функция создает линейный фрактал. Вчитайся в код, чтобы понять концепцию рекурсии.
def line(start, end):
    # Для начала нам необходимо получить размер полного вектора, чтобы проверить его на минимальный порог.
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    if distance < 4:
        # Если ниже порогового размера, то просто построим линию вдоль вектора и закончим (возврат из функции).
        hero.toggleFlowers(False)
        hero.moveXY(start.x, start.y)
        hero.toggleFlowers(True)
        hero.moveXY(end.x, end.y)
        return

    # Иначе мы создадим наш фрактал, используя вектор половинной длины.
    half = Vector.divide(full, 2)

    # Мы создадим 4 линейных фрактала (старт -> А, А -> В, В -> А, и А -> конец), следовательно, нужно будет рассчитать промежуточные позиции А и В.
    A = Vector.add(half, start)

    # Чтобы получить В, необходимо развернуть половину вектора на 90 градусов и умножить на 2/3 (в итоге получится 1/3 полной длины вектора), после прибавить полученный вектор к А.
    rotate = Vector.rotate(half, degreesToRadians(90))
    rotate = Vector.multiply(rotate, 2 / 3)
    B = Vector.add(rotate, A)

    # Теперь просто построй 4 линии, используя функции линий.
    line(start, A)
    line(A, B)
    line(B, A)
    line(A, end)


def flake(start, end):
    # Для создания шестиугольной снежинки нужно создать 6 линейных фракталов, каждый раз поворачивая на 60 градусов.
    side = Vector.subtract(end, start)
    a = start
    b = end
    for i in range(6):
        line(a, b)
        # Чтобы получить следующую грань, необходимо развернуть сторону на 60 градусов.
        # Теперь нужно переназначить `a` и `b` на начальную и конечную точки новой стороны.
        a = b
        side = Vector.rotate(side, degreesToRadians(60))
        b = Vector.add(side, a)


whiteXs = [Vector(12, 10), Vector(60, 10)]
redXs = [Vector(64, 52), Vector(52, 52)]

# Для построения граней придётся вызывать функции с указанием начального и конечного вектора.
flake(redXs[0], redXs[1])
# Используй объекты `Vector`, простые объекты в данном случае не подойдут.
line(whiteXs[0], whiteXs[1])
# Refresh often to avoid a memory leak and crash (working on it)
