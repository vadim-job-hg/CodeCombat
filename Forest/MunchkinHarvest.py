# http://codecombat.com/play/level/munchkin-harvest
# Рассекай манчкинов чтобы выжить!
# Убедись что у тебя достаточно брони.
loop:
target = hero.findNearest(hero.findEnemies())
if target:
    if (self.isReady("cleave")):
        self.cleave(target)
    else:
        self.shield()
