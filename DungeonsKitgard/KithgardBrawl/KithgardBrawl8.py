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


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


def attack(target):
    if target:
        if (hero.distanceTo(target) < 10 and hero.isReady("bash")):
            hero.bash(target)


buildTypes = ["fire-trap"]


def buildTroops():
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 20:
        type = buildTypes[len(hero.built) % len(buildTypes)]
        if hero.gold > hero.costOf(type):
            hero.buildXY(type, enemy.pos.x, enemy.pos.y)


while True:
    items = hero.findItems()
    if len(items) > 0 and hero.health < hero.maxHealth * 0.4:
        pickUpNearestItem(items)
    else:
        attack(hero.findNearestEnemy())
    buildTroops()
