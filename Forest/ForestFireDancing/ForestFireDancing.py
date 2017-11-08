# http://codecombat.com/play/level/forest-fire-dancing
# In this level the evilstone is bad! Avoid them walking the other direction.
while True:
    # evilstone = hero.findNearestItem()
    evilstone = hero.findNearestItem()
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:
            # If the evilstone is on the left, go to the right side.
            hero.moveXY(46, hero.pos.y)
            pass
        else:
            # If the evilstone is on the right, go to the left side.
            hero.moveXY(34, hero.pos.y)
            pass
    else:
        # If there's no evilstone, go to the middle.
        hero.moveXY(40, hero.pos.y)
        pass
