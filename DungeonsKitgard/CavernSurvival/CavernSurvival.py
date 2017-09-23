# http://codecombat.com/play/level/cavern-survival
def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


summonTypes = ['griffin-rider', 'soldier', 'archer']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for soldier in hero.findFriends():
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)


def attack(target):
    if (not target or hero.distanceTo(target) > 20):
        hero.buildXY('caltrops', hero.pos.x, hero.pos.y)
    elif (hero.distanceTo(target) > 10):
        moveTo(target.pos)
    else:
        hero.attack(target)


while True:
    summonTroops()
    commandTroops()
    attack(hero.findNearestEnemy())
