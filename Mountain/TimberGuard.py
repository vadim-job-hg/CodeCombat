loop:
    # Собирай золото.
    item = self.findNearest(self.findItems())
    if(item):
        if(self.isReady("jump")):
            self.jumpTo({'x':item.pos.x, 'y':item.pos.y})
        else:
            self.move(item.pos)
    # Если золота достаточно, призывай солдат.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")
    for friend in self.findFriends():
        down = True;
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            if(enemy):
                self.command(friend, "attack", enemy)
            elif(down):
                self.command(friend, "move", {'x':69, 'y':42})
                down = False
            else:
                self.command(friend, "move", {'x':69, 'y':53})
                down = True
