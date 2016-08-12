# Дай якам подойти поближе, а после отойди на 10 м. вправо чтобы увернуться.
# Увернись от 4 яков, чтобы завершить уровень.

while True:
    enemy = self.findNearestEnemy()
    dist = self.distanceTo(enemy)
    if (dist < 10):
        x = self.pos.x + 10
        y = self.pos.y
        self.moveXY(x, y)
