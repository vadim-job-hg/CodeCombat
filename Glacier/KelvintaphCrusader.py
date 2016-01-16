#http://codecombat.com/play/level/kelvintaph-crusader
# Вы можете находить друзей сквозь стены. Но не врагов.
# Берегитесь гладких, скользких ледяных участков!
# commands attack
def moveTo(position, fast = True):
    if(self.isReady("jump") and fast):
        self.jumpTo(position)
    else:
        self.move(position)
def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        enemies = self.findEnemies()
        witch = self.findNearest(self.findByType('witch'))
        if len(enemies)>0 and witch:
            if friend.type=='paladin':
                CommandPaladin(friend)
            else:
                CommandSoldier(friend)
        elif self.now()<10 and self.now()>5 and friend.type=='paladin':
            if(friend.canCast("heal")):
                self.command(friend, "cast", "heal", friend)
            elif self.now()<7:   
                self.command(friend, "move", {'x':31, 'y':40})
            elif self.now()<12:
                self.command(friend, "move", {'x':7, 'y':40})
        elif self.now()<15 and friend.type!='archer':
            worst = findWorstEnemy()
            if(worst and friend.pos.x-worst.pos.x<10):
                self.command(friend, "move", {'x':50, 'y':58})
        elif friend.type=='archer' and self.now()<15:
            if self.now()<7:
                self.command(friend, "move", {'x':6, 'y':58})
            else:
                self.command(friend, "move", {'x':49, 'y':58})
        elif self.now()<17:
            self.command(friend, "move", {'x':50, 'y':39})
        else:
            self.command(friend, "move", {'x':78, 'y':40})
def CommandPaladin(paladin):
    if(paladin.canCast("heal")):
        target = lowestHealthFriend()
        if target:
            self.command(paladin, "cast", "heal", target)
    elif(paladin.health<100):
        self.command(paladin, "shield")
    else:
        target = findWorstEnemy()
        if(target):
            self.command(paladin, "attack", target)
def CommandSoldier(soldier):
    target = findWorstEnemy()
    if(target):
        self.command(soldier, "attack", target)
def findWorstEnemy():
    witch = self.findNearest(self.findByType('witch'))
    ogre = self.findNearest(self.findByType('ogre'))
    skeleton = self.findNearest(self.findByType('skeleton'))
    if witch:
        return witch
    elif ogre:
        return ogre
    elif skeleton:
        return skeleton
    else:
        return None
def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend
def attack(target):
    if target:
        if(self.distanceTo(target)>10):
            moveTo(target.pos)
        elif(self.isReady("bash")):
            self.bash(target)
        else:
            self.attack(target)

loop:
    commandTroops()
    brawler = self.findNearest(self.findByType('brawler'))
    catapult = self.findNearest(self.findByType('catapult'))
    if brawler and self.distanceTo(brawler)>15:
        moveTo(brawler.pos, False)
    elif brawler:
        runaway = Vector.subtract(self.pos, brawler.pos)
        runaway = Vector.normalize(runaway)
        runaway = Vector.multiply(runaway, 15)
        direction = Vector.add(runaway, self.pos)
        moveTo(direction, False)
    elif catapult:
        attack(catapult)
    else:
        self.move({'x':78, 'y':15})


