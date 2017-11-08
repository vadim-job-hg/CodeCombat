while True:  # Собирай золото.
    item = hero.findNearestItem()
    if (item):
        if (hero.isReady("jump")):
            hero.jumpTo({'x': item.pos.x, 'y': item.pos.y})
        else:
            hero.move(item.pos)
    # Если золота достаточно, призывай солдат.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    for friend in hero.findFriends():
        down = True;
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            if (enemy):
                hero.command(friend, "attack", enemy)
            elif (down):
                hero.command(friend, "move", {'x': 69, 'y': 42})
                down = False
            else:
                hero.command(friend, "move", {'x': 69, 'y': 53})
                down = True
