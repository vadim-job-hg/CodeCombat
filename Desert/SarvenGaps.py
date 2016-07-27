# http://codecombat.com/play/level/sarven-gaps
# Двигайся к оазису короткими перебежками по 10 м.
# Строй заграждения на 20 м. левее огра.

while True:
    enemy = self.findNearestEnemy()
    if enemy:
        # Строй заграждения на 20 м. левее врага.
        self.buildXY('fence', enemy.pos.x - 20, enemy.pos.y)
        pass
    else:
        # Передвигайся на 10 метров за ход.
        self.moveXY(self.pos.x, self.pos.y - 10)
        pass
