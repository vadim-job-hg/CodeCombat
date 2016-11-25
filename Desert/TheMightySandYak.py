# Дай якам подойти поближе, а после отойди на 10 м. вправо чтобы увернуться.
# Увернись от 4 яков, чтобы завершить уровень.

while True:
    enemy = hero.findNearestEnemy()
    dist = hero.distanceTo(enemy)
    if (dist < 10):
        x = hero.pos.x + 10
        y = hero.pos.y
        hero.moveXY(x, y)
