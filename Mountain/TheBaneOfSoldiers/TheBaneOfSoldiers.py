# Robobombs explode when they die or touch an enemy.
# Split up your soldiers so that they don't all get exploded together.
def commandSoldier(soldier, index):
    target = hero.findNearestEnemy()
    if (target and index == 0):
        hero.command(soldier, "attack", target)
    else:
        hero.command(soldier, "move", {'x': 15, 'y': 30})


while True:
    friends = hero.findFriends()
    for index, friend in enumerate(friends):
        commandSoldier(friend, index)
