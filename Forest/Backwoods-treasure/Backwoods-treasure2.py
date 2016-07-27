middleX = 61
middleY = 52
loop:
enemy = self.findNearest(self.findEnemies())
item = self.findNearest(self.findItems())
flag = self.findFlag()
if (enemy):
    dist = self.distanceTo(enemy);
if (enemy and dist < 10):
    if (self.isReady("cleave")):
        self.cleave(enemy)
    elif (self.isReady("bash")):
        self.bash(enemy)
    elif (self.isReady("power-up")):
        self.powerUp()
        self.attack(enemy)
    else:
        self.attack(enemy)
elif (item):
    self.move(item.pos)
elif (True):
    self.moveXY(middleX, middleY)
