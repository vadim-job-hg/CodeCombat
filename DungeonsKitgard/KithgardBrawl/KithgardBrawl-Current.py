def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)


def CommandPaladin(paladin):
    enemy = paladin.findNearestEnemy()
    if (paladin.canCast("heal") and hero.health < hero.maxHealth):
        hero.command(paladin, "cast", "heal", hero)
    else:
        hero.command(paladin, "shield")


def pickUpNearestItem(items):
    hero.shield()


def attack(target):
    if target:
        if (hero.distanceTo(target) < 10 and hero.isReady("bash")):
            hero.bash(target)


def runAway():
    enemy = hero.findNearestEnemy()
    if enemy:
        goal = Vector.subtract(enemy.pos, hero.pos)
        goal = Vector.normalize(goal)
        goal = Vector.multiply(goal, 10)
        moveToPos = Vector.add(hero.pos, goal)
        hero.move(moveToPos)


buildTypes = ["fire-trap"]


def buildTroops():
    enemy = hero.findNearest(hero.findEnemies())
    items = hero.findItems()
    paladins = hero.findByType('paladin')
    if len(items) > 0 and hero.distanceTo(items[0]) < 10:
        pickUpNearestItem(items)
    elif len(paladins) > 0:
        hero.shield()
    elif (enemy and hero.canCast('chain-lightning', enemy) and hero.distanceTo(enemy) < 20):
        hero.cast('chain-lightning', enemy)
    elif enemy and hero.distanceTo(enemy) < 10:
        type = buildTypes[len(hero.built) % len(buildTypes)]
        if hero.gold > hero.costOf(type):
            hero.buildXY(type, hero.pos.x, hero.pos.y)
            if (type == 'fire-trap'):
                hero.shield()
        else:
            pickUpNearestItem(items)
    else:
        pickUpNearestItem(items)


def onSpawn(event):
    while True:
        potion = pet.findNearestByType("potion")
        if potion and hero.health < hero.maxHealth / 2:
            pet.fetch(potion)


pet.on("spawn", onSpawn)

while True:
    if hero.health < hero.maxHealth / 2:
        summonTroops()
    commandTroops()
    if (hero.canCast('earthskin', self)):
        hero.cast('earthskin', self)
    buildTroops()