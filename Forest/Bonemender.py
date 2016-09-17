# https://codecombat.com/play/level/bonemender
# Лечите дружественных солдат, чтобы победить в осаде.
while True:
    if hero.canCast("regen"):
        bernardDistance = hero.distanceTo("Bernard")
        if bernardDistance < 10:
            # Бернарду нужна регенерация!
            hero.cast("regen", "Bernard")
        chandraDistance = hero.distanceTo("Chandra")
        if chandraDistance < 10:
            # Бернарду нужна регенерация!
            hero.cast("regen", "Chandra")
            # Используйте "if" и "distanceTo" для регенерации "Chandra"
            # Если она ближе 10 метров.
    else:
        enemy = hero.findNearest(hero.findEnemies())
        if(enemy and hero.distanceTo(enemy)<20):
            hero.attack(enemy)
# Если вы не колдуете "regen", используйте "if" и "distanceTo"
# чтобы атаковать врагов, которые ближе, чем hero.attackRange.
