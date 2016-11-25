# http://codecombat.com/play/level/munchkin-harvest
# Рассекай манчкинов чтобы выжить!
# Убедись что у тебя достаточно брони.
while True:
    target = hero.findNearest(hero.findEnemies())
    if target:
        if (hero.isReady("cleave")):
            hero.cleave(target)
        else:
            hero.shield()
