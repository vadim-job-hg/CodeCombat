# http://codecombat.com/play/level/kelvintaph-burgler
# Что это за жуткие артефакты? Не дайте им взорвать себя!
# Ледяные врата откроются, когда оба огра будут мертвы.
coors1 = [0, 0]
coors2 = [0, 0]


def moveTo(position, fast=True):
    if (self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)


summonTypes = ['soldier']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


def сommandTroops():
    for index, friend in enumerate(self.findFriends()):
        if chieftain and friend.type != 'paladin':
            continue
        if witch and friend.type != 'paladin':
            continue
        if chieftain and chieftain.pos.x < 57 and chieftain.pos.x > 43:
            self.command(friend, "move", {'x': 25, 'y': 48})
        elif not chieftain and friend.pos.x < 40:
            self.command(friend, "move", {'x': 51, 'y': 51})
        elif friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier':
            if friend.pos.y > 30:
                CommandSoldier(friend)
            else:
                KillRobots(friend)
        else:
            CommandArcher(friend)


def CommandPaladin(paladin):
    if (paladin.canCast("heal") and not chieftain):
        target = lowestHealthFriend()
        if target:
            self.command(paladin, "cast", "heal", target)
    elif (paladin.health < 100):
        self.command(paladin, "shield")
    else:
        if witch:
            self.command(paladin, "attack", witch)
        elif (chieftain):
            self.command(paladin, "attack", chieftain)
        else:
            self.command(paladin, "move", {'x': 78, 'y': 40})


def CommandSoldier(soldier):
    if witch:
        self.command(soldier, "attack", witch)
    else:
        self.command(soldier, "move", {'x': 78, 'y': 40})


def CommandArcher(soldier):
    if witch:
        self.command(soldier, "attack", witch)
    else:
        self.command(soldier, "move", {'x': 78, 'y': 40})


def KillRobots(soldier):
    robot = self.findNearest(self.findEnemies())
    if robot:
        self.command(soldier, "attack", robot)


def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend


def RunFrom():
    missiles = self.findEnemyMissiles()
    missle = self.findNearest(missiles)
    if len(missiles) > 0:
        coors1[0] = missle.pos.x
        coors1[1] = missle.pos.y
        y = findTheY(coors1[0], coors2[0], coors1[1], coors2[1], self.pos.x)
        if y > 15:
            moveTo({'x': self.pos.x, 'y': 10}, False)
        else:
            moveTo({'x': self.pos.x, 'y': 20}, False)
        coors2[0] = coors1[0]
        coors2[1] = coors1[1]


def RunTrought():
    robots = self.findByType('robot-walker')
    summonTroops()
    up = True
    mid = True
    douwn = True
    for robot in robots:
        if (robot.pos.y < 20 and robot.pos.y > 10):
            mid = False
        if (robot.pos.y > 20):
            up = False
        if (robot.pos.y < 10):
            down = False
    if (mid):
        coorY = 15
    if (down):
        coorY = 6
    if (up):
        coorY = 22
    if (self.pos.x < 16):
        self.moveXY(16, coorY)
    elif (self.pos < 59):
        moveTo({'x': 60, 'y': coorY}, False)
    else:
        moveTo({'x': 79, 'y': 14}, False)


def findTheY(x1, x2, y1, y2, x):
    if (y2 != y1):
        y = (x - x1) / (x2 - x1) * (y2 - y1) + y1
    else:
        y = y1
    return y


def findTheMiddle(pos1, pos2):
    return {'x': (pos1.x + pos2.x) / 2, 'y': (pos1.y + pos2.y) / 2}


loop:  # self.say(self.findEnemies()[0].type)
witch = self.findNearest(self.findByType('witch'))
chieftain = self.findNearest(self.findByType('chieftain'))
if witch or chieftain:
    RunFrom()
else:
    RunTrought()
сommandTroops()
