loop:
yak = self.findNearestEnemy()
if yak:
    if yak.pos.y > self.pos.y:
        self.buildXY('fence', self.pos.x, yak.pos.y - 10)
    if yak.pos.y < self.pos.y:
        self.buildXY('fence', self.pos.x, yak.pos.y + 10)
    pass
else:
    self.moveXY(self.pos.x + 10, self.pos.y)
