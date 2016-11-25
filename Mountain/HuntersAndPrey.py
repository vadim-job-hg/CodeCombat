# http://codecombat.com/play/level/hunters-and-prey

def pickUpCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)


def summonTroops():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")


# This function has an argument named soldier.
# Arguments are like variables.
# The value of an argument is determined when the function is called.
def commandSoldier(soldier):
    enemy = soldier.findNearestEnemy()
    if enemy:
        hero.command(soldier, "attack", enemy)


# Write a commandArcher function to tell your archers what to do!
# It should take one argument that will represent the archer passed to the function when it's called.
# Archers should only attack enemies who are closer than 25 meters, otherwise, stay still
def commandArcher(soldier):
    enemy = soldier.findNearestEnemy()
    if enemy and soldier.distanceTo(enemy) < 25:
        hero.command(soldier, "attack", enemy)


while True:
    pickUpCoin()
    summonTroops()
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < 100 and (friend.type == "soldier"):
            hero.command(friend, "defend", hero.pos)
        elif friend.type == "soldier":
            # This friend will be assigned to the variable soldier in commandSoldier
            commandSoldier(friend)
        elif friend.type == "archer":
            commandArcher(friend)
