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
        if enemy:
            hero.command(soldier, "attack", enemy)


def attack(target):
    if (hero.distanceTo(target) > 10):
        moveTo(target.pos)
    else:
        hero.attack(target)


while True:
    summonTroops()
    commandTroops()
    enemy = hero.findNearestEnemy()
    if (enemy):
        attack(enemy)
