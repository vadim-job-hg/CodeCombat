# http://codecombat.com/play/level/bookkeeper
def attack(target):
    if target:
        if (self.isReady("bash")):
            self.bash(target)
        elif (self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        else:
            self.attack(target)


eCount = 0
iCount = 0
self.wait(1)
while True:  # enemy = self.findNearestEnemy()
    enemy = self.findNearest(self.findEnemies())
    # item  = self.findNearestItem()
    item = self.findNearest(self.findItems())
    if (enemy):
        attack(enemy)
        attack(enemy)
        eCount = eCount + 1
        iCount = 0
        self.wait(1)
    elif (item and self.now() <= 30):
        self.moveXY(item.pos.x, item.pos.y)
        iCount = self.gold
        eCount = 0
    else:
        self.moveXY(59, 33)
        if (eCount > 0 or iCount > 0):
            self.say(eCount + iCount)
