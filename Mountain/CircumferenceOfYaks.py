# https://codecombat.com/play/level/circumference-of-yaks

# Вычисли длины окружностей яков.

# Первый круг яков.
yak1 = hero.findNearestEnemy()
# Дистанция до яка равна радиусу.
radius1 = hero.distanceTo(yak1)
# Длина окружности вычисляется так:
circumference1 = 2 * Math.PI * radius1
# Скажи результат.
hero.say(circumference1)

# Двигайся к следующей отметке.
hero.moveXY(60, 34)
# Найди яка из второго круга.
yak2 = hero.findNearestEnemy()
# Найди радиус второй окружности.
radius2 = hero.distanceTo(yak2)
# Вычисли длину второй окружности.
circumference2 = 2 * Math.PI * radius2
# Скажи результат.
hero.say(circumference2)
