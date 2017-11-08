# https://codecombat.com/play/level/perilous-passage
# Rally the peasants to protect their home!
# Have them build only 1 trap between them and the enemy.
def findTheMiddle(pos1, pos2):
    return {'x': (pos1.x + pos2.x) / 2, 'y': (pos1.y + pos2.y) / 2}
friends = hero.findFriends()
for friend in friends:
    xPos = friend.pos.x
    yPos = friend.pos.y
    friend["startPos"] = {"x":xPos, "y":yPos}

while True:
    enemies = hero.findEnemies()
    for enemy in enemies:
        friend = enemy.findNearest(friends)
        if hero.isPathClear(friend.pos, enemy.pos):
            if not enemy.accountedFor:
                # Command the friend to build a firetrap
                # at the midpoint between them and enemy.
                mid = findTheMiddle(friend.pos, enemy.pos)
                hero.command(friend, 'buildXY', 'fire-trap', mid.x, mid.y)
                enemy["accountedFor"] = True;
        else:
            # Otherwise, command the friend to move back
            # to their .startPos property:
            hero.command(friend, 'move',friend["startPos"] )
