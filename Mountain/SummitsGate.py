summonTypes = ['griffin-rider']
tactick = 'hold'
stage = 1


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend
    return lowestFriend


def commandPaladin(paladin):
    if (paladin.canCast("heal")):
        if (self.health < self.maxHealth * 0.8):
            target = self
        else:
            target = lowestHealthPaladin()
        if target:
            self.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        self.command(paladin, "shield")
    elif stage < 4:
        self.command(paladin, "move", {'x': 94, 'y': 34})
    elif stage == 5:
        self.command(paladin, "move", {'x': 284, 'y': 33})
    else:
        target = self.findNearest(self.findEnemies())
        if (warlock):
            target = warlock
        if (target):
            self.command(paladin, "attack", target)


def commandSoldier(soldier):
    target = self.findNearest(self.findEnemies())
    if (warlock):
        target = warlock
    if stage == 3:
        self.command(soldier, "move", {'x': 84, 'y': 34})
    elif (target):
        self.command(soldier, "attack", target)


def commandFriends():
    friends = self.findFriends()
    for friend in friends:
        if tactick == 'hold':
            self.command(friend, "defend", {'x': 1, 'y': 40})
        elif friend.type == "paladin":
            commandPaladin(friend)
        else:
            commandSoldier(friend)


def moveTo(position):
    if (self.isReady("jump")):
        self.jumpTo(position)
    else:
        self.move(position)


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(target.pos)
        else:
            self.attack(target)


def pickUpNearestItem():
    nearestItem = self.findNearest(self.findItems())
    if nearestItem:
        moveTo(nearestItem.pos)


commandFriends()
self.moveXY(31, 56)
loop:
catapult = self.findNearest(self.findByType('catapult'))
warlock = self.findNearest(self.findByType('warlock'))
target = self.findNearest(self.findEnemies())
nearestItem = self.findNearest(self.findItems())
now = self.now()
if catapult:
    stage = 1
    attack(catapult)
elif now < 20:
    tactick = 'defend'
    stage = 2
    moveTo({"x": 50, "y": 33})
elif stage < 4:
    if target:
        stage = 3
        attack(target)
    else:
        moveTo({"x": 172, "y": 46})
    if self.pos.x > 170:
        stage = 4
elif stage < 5:
    if self.pos.x < 240:
        moveTo({"x": 274, "y": 35})
        tactick = 'defend'
    elif nearestItem and self.distanceTo(nearestItem) < 10:
        pickUpNearestItem()
        tactick = 'attack'
    elif (warlock):
        target = warlock
        summonTroops()
        attack(target)
    elif target and target.type != 'gates':
        attack(target)
    elif nearestItem and self.distanceTo(nearestItem) < 45:
        pickUpNearestItem()
        tactick = 'defend'
        summonTroops()
    else:
        attack(target)
    if self.pos.x > 290:
        stage = 5
    tactick = 'attack'
else:
    summonTroops()
    attack(target)
commandFriends()
