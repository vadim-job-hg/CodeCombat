# https://codecombat.com/play/level/unfair-support
# Идите украдкой через лес и устройте засаду шаману.
# Слушайте командира Крейга для предупреждения о надвигающихся врагах.

# Размещайте флаги, после того, как нажмёте "ЗАПУСТИТЬ".
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        # Подберите флаг.
        hero.pickUpFlag(flag)
        pass
    elif enemy:
        # Атакуйте врагов на месте.
        hero.attack(enemy)
        pass
