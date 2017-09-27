# https://codecombat.com/play/level/fractalization
# Сверьтесь с руководством для описания проблемы.
# Вот несколько функций, которые помогут чертить кривые.

def degreesToRadians(degrees):
    # Все операции с векторами предпочтительнее выполнять в радианах, нежели в градусах.
    return Math.PI / 180 * degrees


def koch(start, end):
    # Эта функция начертит кривую Коха между двумя векторами.
    # Начните с создания вектора от начальной до конечной точек, используя Vector.subtract.
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    # Проверяйте величину вектора, для определения точки остановки.
    if distance < 3:
        # Перемещайтесь на позицию и чертите линию. Не забудьте вовремя переходить по точкам.
        hero.toggleFlowers(False)
        hero.moveXY(start.x, start.y)
        hero.toggleFlowers(True)
        hero.moveXY(end.x, end.y)
        return

        # Необходимо начертить 4 кривых Коха со сторонами 1/3 длины.
    # Рассчитаем три промежуточные точки: А, В и С.
    # Нам нужна точка, которая находится на расстоянии одной третьей полного вектора, от его начала.
    third = Vector.multiply(full, 1 / 3)
    A = Vector.add(start, third)
    # Этот вектор нужно развернуть на 60 градусов от точки А, но оставить ту же длину. Используйте поворот и добавление вектора, чтобы получить точку В.
    B = Vector.add(A, Vector.rotate(third, degreesToRadians(60)))
    # Эту точку можно получить, прибавив еще одну треть полного вектора к точке А.
    C = Vector.add(A, third)
    # Теперь мы можем начертить 4 кривых, соединяющих стартовую точку, точки А, В, С и конечную точку.
    koch(start, A);
    koch(A, B);
    koch(B, C);
    koch(C, end);


whiteXs = [Vector(6, 6), Vector(74, 6), Vector(74, 61), Vector(6, 61)]
hero.setFlowerColor("white");
koch(whiteXs[0], whiteXs[1]);
koch(whiteXs[1], whiteXs[2]);
koch(whiteXs[2], whiteXs[3]);
koch(whiteXs[3], whiteXs[0]);
