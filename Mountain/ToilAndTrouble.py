def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(target)
        elif (hero.isReady("cleave")):
            hero.cleave(target)
        else:
            hero.attack(target)


def chooseTarget(friend):
    # the code errors is allright
    if friend.type == "archer":
        if len(hero.findByType("thrower")) > 0:
            return friend.findNearest(friend.findByType("thrower"))
        elif len(hero.findByType("witch")) > 0:
            return friend.findNearest(friend.findByType("witch"))
        else:
            return friend.findNearest(hero.findEnemies())
    elif friend.type == "soldier":
        return friend.findNearest(hero.findByType("witch"))


# Define a chooseTarget function which takes a friend argument
# Returns the a target to attack, depending on the type of friend.
# Soldiers should attack the witches, archers should attack nearest enemy.


while True:
    friends = hero.findFriends()
    for friend in friends:
        # Use your chooseTarget function to decide what to attack.
        enemy = chooseTarget(friend)
        if (enemy):
            hero.command(friend, 'attack', enemy)
    attack(hero.findNearestEnemy())
