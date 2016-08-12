while True:
    flag = self.findFlag()
    if (flag):
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if (item):
            position = item.pos
            x = position.x
            y = position.y
            self.moveXY(x, y)
