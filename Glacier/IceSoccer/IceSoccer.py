# https://codecombat.com/play/level/ice-soccer
def commandAttacker(friend, item):
    flag = hero.findFlag()
    if flag:
        self.command(friend, "move", flag.pos)
        if friend.distanceTo(flag) < 2:
            hero.removeFlag(flag)
    else:
        if item.pos.x > friend.pos.x:
            self.command(friend, "move", item.pos)
        else:
            self.command(friend, "move", Vector(27, 38))


# Управляйте крестьянами, чтобы не позволить ограм забить гол.
# Тип огненного шара (файербол) - "ball"
def commandSoldiers(x, y, base=False):
    move = 0;
    for index, friend in enumerate(self.findFriends()):
        if (index == 1 and y > 36):
            if base:
                self.command(friend, "move", {'x': 18, 'y': 43})
            else:
                self.command(friend, "move", {'x': x, 'y': y})
        elif y <= 36 and index == 0:
            if base:
                self.command(friend, "move", {'x': 18, 'y': 39})
            else:
                self.command(friend, "move", {'x': x, 'y': y})


def findTheY(x1, x2, y1, y2, x):
    if (y2 != y1):
        y = (x - x1) / (x2 - x1) * (y2 - y1) + y1
    else:
        y = y1
    return y


friends = self.findFriends()
pos1 = []
pos2 = []
while True:
    base = False
    item = self.findNearest(self.findByType('ball'))
    if pos2[1] != item.pos.y or pos2[0] != item.pos.x:
        pos1[0] = pos2[0]
        pos1[1] = pos2[1]
        pos2[0] = item.pos.x
        pos2[1] = item.pos.y
    if len(pos1) > 0 and len(pos2) > 0:
        yCatch = findTheY(pos1[0], pos2[0], pos1[1], pos2[1], 18)
        if yCatch > 50:
            yCatch = 50 - (yCatch - 50)
        elif yCatch < 20:
            yCatch = 20 - (20 - yCatch)
        if (yCatch > 44 or yCatch < 28):
            yCatch = 39
        # self.say(yCatch)
        if (item and yCatch):
            if pos2[1] > pos1[1] and yCatch > 5 and yCatch < 20:
                base = True
            commandSoldiers(18, yCatch, base)
    commandAttacker(friends[2], item)
