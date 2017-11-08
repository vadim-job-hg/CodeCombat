while True:
    flag = hero.findFlag()
    if (flag):
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()
        if (item):
            position = item.pos
            x = position.x
            y = position.y
            hero.moveXY(x, y)
