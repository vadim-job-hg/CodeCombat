# https://codecombat.com/play/level/bonemender
# Лечите дружественных солдат, чтобы победить в осаде.
while True:
    if hero.canCast("regen"):
        bernardDistance = hero.distanceTo("Bernard")
        if bernardDistance < 10:
            # Бернарду нужна регенерация!
            hero.cast("regen", "Bernard")
        chandraDistance = hero.distanceTo("Chandra")
        # Используйте "if" и "distanceTo" для регенерации "Chandra"
        # Если она ближе 10 метров.
        if chandraDistance < 10:
            hero.cast("regen", "Chandra")

    else:
        # Если вы не колдуете "regen", используйте "if" и "distanceTo"
        # чтобы атаковать врагов, которые ближе, чем hero.attackRange.
        enemy = hero.findNearestEnemy()
        if enemy and hero.distanceTo(enemy) < hero.attackRange:
            hero.attack(enemy)
