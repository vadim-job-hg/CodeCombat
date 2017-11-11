# https://codecombat.com/play/level/shrapnel
# Используй заряды, чтобы накрыть группу огров.
# Тогда подстрели их из лука.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("throw"):
            distance = hero.distanceTo(enemy)
            # Бросай, если огры дальше 15 м.
            # Используй `if`, чтобы сравнить дистанцию с 15.
            if distance>15:
                hero.throw(enemy)
            # Используй `else`, чтобы атаковать, если не бросаешь.
            else:
                hero.attack(enemy)
        else:
            hero.attack(enemy)
