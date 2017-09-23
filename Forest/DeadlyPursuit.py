# http://codecombat.com/play/level/deadly-pursuit
# Собери все монеты и используй флаги для установки ловушек за собой.
# Разберись с этими ограми.

while True:
    flag = hero.findFlag()
    # item = hero.findNearestItem()
    item = hero.findNearestItem()
    if flag:
        hero.buildXY('fire-trap', flag.pos.x, flag.pos.y)
        hero.pickUpFlag(flag)
    elif item:
        hero.moveXY(item.pos.x, item.pos.y)
