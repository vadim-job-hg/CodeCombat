# http://codecombat.com/play/level/orge-rush
# Should fill in some default source
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
            self.shield()


loop:
enemy = self.findNearest(self.findEnemies())
if enemy:
    attack(enemy)
