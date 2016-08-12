# Robobombs explode when they die or touch an enemy.
# Split up your soldiers so that they don't all get exploded together.
def commandSoldier(soldier, index):
    target = self.findNearest(self.findEnemies())
    if (target and index == 0):
        self.command(soldier, "attack", target)
    else:
        self.command(soldier, "move", {'x': 15, 'y': 30})


while True:
    friends = self.findFriends()
    for index, friend in enumerate(friends):
        commandSoldier(friend, index)
