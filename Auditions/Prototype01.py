# http://codecombat.com/play/level/prototype-01
def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo(position) > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (self.isReady("bash")):
            self.bash(target)
        elif (self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        elif (self.isReady("attack")):
            self.attack(target)
        else:


loop:
flag = self.findFlag()
if flag:
    self.pickUpFlag(flag)
else:
    enemy = self.findNearest(self.findEnemies())
    if enemy:
        attack(enemy)
        # find some enemy to attack
        # use cleave when ready
