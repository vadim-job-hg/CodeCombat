while True:
    flag = self.findFlag();
    if (flag):
        self.buildXY("fire-trap", flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if (item):
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            self.moveXY(itemX, itemY)
