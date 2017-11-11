# http://codecombat.com/play/level/testbraen
def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        elif (hero.isReady("attack")):
            hero.attack(target)
        else:
            pass

while True:
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    else:
        enemy = hero.findNearestEnemy()
        if enemy:
            attack(enemy)
            # find some enemy to attack
            # use cleave when ready
