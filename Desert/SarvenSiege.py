# Defend your towers in this replayable challenge level!
# Step on an X if you have 20 gold to build a soldier.
array = [[83, 79],[84, 52], [83, 22]]
loop:
    items = self.findItems()
    item = self.findNearest(items)
    if(self.gold<20):
        if(self.isReady('jump')):
            self.jumpTo(item.pos)
        else:
            self.moveXY(item.pos.x, item.pos.y)
    else:
        if(self.pos.y>70):
            self.moveXY(array[0][0], array[0][1])
        elif(self.pos.y>40):
            self.moveXY(array[1][0], array[1][1])
        else:
            self.moveXY(array[2][0], array[2][1])
