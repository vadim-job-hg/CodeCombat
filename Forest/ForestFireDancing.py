#http://codecombat.com/play/level/forest-fire-dancing
#In this level the evilstone is bad! Avoid them walking the other direction.
while True:
    #evilstone = self.findNearestItem()
    evilstone = self.findNearest(self.findItems())
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:
            # If the evilstone is on the left, go to the right side.
            self.moveXY(46, self.pos.y)
            pass
        else:
            # If the evilstone is on the right, go to the left side.
            self.moveXY(34, self.pos.y)
            pass
    else:
        # If there's no evilstone, go to the middle.
        self.moveXY(40, self.pos.y)
        pass
