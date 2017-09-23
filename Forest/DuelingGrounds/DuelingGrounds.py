# http://codecombat.com/play/level/dueling-grounds
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
        if target:
            hero.command(soldier, "attack", target)


def attack(target):
    if (hero.distanceTo(target) > 10):
        moveTo(target.pos)
    elif (hero.isReady("bash")):
        hero.bash(target)
    else:
        hero.attack(target)


while True:
    summonTroops()
    commandTroops()
    target = hero.findNearestEnemy()
    knight = hero.findNearest(hero.findByType('knight'))
    captain = hero.findNearest(hero.findByType('captain'))
    # Enemies = hero.findEnemies()
    # for en in Enemies:
    # hero.say(en.type)
    if (knight and hero.distanceTo(knight) < 20):
        target = knight
    if (captain and hero.distanceTo(captain) < 20):
        target = captain
    attack(target)
