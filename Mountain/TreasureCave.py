# https://codecombat.com/play/level/treasure-cave?
# Огр даже не сопротивлялся! От этого йети стоит держаться подальше.

# Огненные ловушки настроены на взрыв через 5 секунд.
# Поляна на севере отлично подойдёт для отвлекающего манёвра.
# Йети ушёл не навсегда, так что торопись и хватай монеты!
hero.buildXY('fire-trap', 64, 44)
hero.moveXY(73, 15)
hero.moveXY(42, 11)
hero.moveXY(46, 9)
hero.wait(1)
hero.moveXY(14, 37)
item = hero.findNearestItem()
hero.jumpTo(Vector(17, 37))
while item:
    hero.move(item.pos)
    item = hero.findNearestItem()
hero.moveXY(73, 15)
