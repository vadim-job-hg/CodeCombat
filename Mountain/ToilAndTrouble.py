def moveTo(position, fast=True):
    if (self.isReady("jump") and self.distanceTo > 10 and fast):
        self.jumpTo(position)
    else:
        self.move(position)


def attack(target):
    if target:
        if (self.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (self.isReady("bash")):
            self.bash(target)
        elif (self.isReady("power-up")):
            self.powerUp()
            self.attack(target)
        elif (self.isReady("cleave")):
            self.cleave(target)
        else:
            self.attack(target)


def chooseTarget(friend):
    # the code errors is allright
    if friend.type == "archer":
        if len(self.findByType("thrower")) > 0:
            return friend.findNearest(friend.findByType("thrower"))
        elif len(self.findByType("witch")) > 0:
            return friend.findNearest(friend.findByType("witch"))
        else:
            return friend.findNearest(self.findEnemies())
    elif friend.type == "soldier":
        return friend.findNearest(self.findByType("witch"))


# Define a chooseTarget function which takes a friend argument
# Returns the a target to attack, depending on the type of friend.
# Soldiers should attack the witches, archers should attack nearest enemy.


loop:
friends = self.findFriends()
for friend in friends:
    # Use your chooseTarget function to decide what to attack.
    enemy = chooseTarget(friend)
    if (enemy):
        self.command(friend, 'attack', enemy)
attack(self.findNearest(self.findEnemies()))
