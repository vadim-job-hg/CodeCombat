def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider' or friend.type == 'skeleton':
            CommandSoldier(friend)


def CommandSoldier(soldier):
    enemy = soldier.findNearestEnemy()
    if enemy:
        self.command(soldier, "attack", enemy)
    else:
        self.command(soldier, "defend", hero)
    pass


# todo: use peasant here
def pickUpNearestItem(items):
    nearestItem = self.findNearest(items)
    if nearestItem and (nearestItem.pos.x < 38 or nearestItem.pos.y < 33):
        moveTo(nearestItem.pos)
    else:
        moveTo({'x': 28, 'y': 33})


def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo(position) > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


def action():
    target = self.findNearest(self.findEnemies())
    if (hero.canCast('summon-burl', hero)):
        hero.cast('summon-burl')
    elif (hero.canCast('summon-undead')):
        hero.cast('summon-undead')
    elif (target and hero.canCast('fear', target)):
        hero.cast('fear', target)


def onSpawn(event):
    index = 0
    while True:
        pet.moveXY(46, 26)
        pet.moveXY(50, 9)
        pet.moveXY(74, 12)
        pet.moveXY(65, 27)
        pet.moveXY(39, 30)
        pet.moveXY(hero.pos.x + 5, hero.pos.y + 5)
        pet.moveXY(hero.pos.x - 5, hero.pos.y - 5)
        pet.moveXY(46, 48)
        pet.moveXY(74, 58)
        pet.moveXY(72, 42)
        pet.moveXY(52, 50)
        pet.moveXY(40, 33)
        pet.moveXY(hero.pos.x + 5, hero.pos.y + 5)
        pet.moveXY(hero.pos.x - 5, hero.pos.y - 5)
        pet.moveXY(24, 21)
        pet.moveXY(6, 29)
        pet.moveXY(29, 57)
        pet.moveXY(11, 58)
        pet.moveXY(22, 19)
        pet.moveXY(hero.pos.x + 5, hero.pos.y + 5)
        pet.moveXY(hero.pos.x - 5, hero.pos.y - 5)


pet.on("spawn", onSpawn)
while True:
    items = self.findItems()
    action()
    commandTroops()
    flag = hero.findFlag();
    if (flag):
        hero.pickUpFlag(flag)
    elif len(items) > 0 and hero.now() > 10:
        pickUpNearestItem(items)
