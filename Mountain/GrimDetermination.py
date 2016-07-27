# http://codecombat.com/play/level/grim-determination
summonTypes = ['griffin-rider']


def summonTroops():
    type = summonTypes[len(self.built) % len(summonTypes)]
    if self.gold > self.costOf(type):
        self.summon(type)


# Найти паладина с самым низким количеством здоровья.
def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = self.findFriends()
    for friend in friends:
        if friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend

    return lowestFriend


def commandPaladin(paladin):
    if (paladin.canCast("heal")):
        target = lowestHealthPaladin()
        if target:
            self.command(paladin, "cast", "heal", target)
    elif (paladin.health < 200):
        self.command(paladin, "shield")
    else:
        target = paladin.findNearestEnemy()
        if (target):
            self.command(paladin, "attack", target)


def commandPeasant(peasant):
    item = peasant.findNearestItem()
    if item:
        self.command(peasant, 'move', item.pos)


def commandGriffin(griffin):
    target = self.findNearest(self.findByType('warlock'))
    if not target:
        target = griffin.findNearestEnemy()
    if (target):
        self.command(griffin, "attack", target)


def commandFriends():
    # Командуй своими союзниками.
    friends = self.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            commandPeasant(friend)
        elif friend.type == "griffin-rider":
            commandGriffin(friend)
        elif friend.type == "paladin":
            commandPaladin(friend)


loop:
commandFriends()
summonTroops()
