# http://codecombat.com/play/level/sarven-gaps
# Двигайся к оазису короткими перебежками по 10 м.
# Строй заграждения на 20 м. левее огра.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Строй заграждения на 20 м. левее врага.
        hero.buildXY('fence', enemy.pos.x - 20, enemy.pos.y)
        pass
    else:
        # Передвигайся на 10 метров за ход.
        hero.moveXY(hero.pos.x, hero.pos.y - 10)
        pass
