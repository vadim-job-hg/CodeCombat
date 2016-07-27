# Прикажите вашим войскам двигаться на восток и атаковать любых огров которых они увидят.
# Используйте for циклы и findFriends.
# Вы можете использовать метод findNearestEnemy() на Ваших солдатах, для того, чтобы находить ближайшего к ним, а не к себе, противника.
index = 0
loop:
friends = self.findFriends()
enemy = self.findNearest(self.findEnemies())
if enemy and self.distanceTo(enemy) < 20:
    if (self.isReady("jump") and self.distanceTo(enemy) > 10):
        self.jumpTo(enemy.pos)
    elif (self.isReady("cleave")):
        self.cleave(enemy)
    elif (self.isReady("bash")):
        self.bash(enemy)
    elif (self.isReady("power-up")):
        self.powerUp()
        self.attack(enemy)
    else:
        self.attack(enemy)
else:
    if (self.now() < 7):
        pos = {'x': 87, 'y': 49}
    else:
        pos = {'x': 12, 'y': 47}
    if (self.isReady("jump")):
        self.jumpTo(pos)
    else:
        self.move(pos)
for j in range(len(friends)):
    friend = friends[j]
    if (friend.pos.y > 46 and self.now() < 5):
        pos = {'x': 12, 'y': 64}
    elif (friend.pos.y > 46):
        if (friend.type != 'archer'):
            pos = {'x': 61, 'y': 67}
        else:
            pos = {'x': 42, 'y': 67}
    else:
        if (friend.type != 'archer'):
            pos = {'x': 45, 'y': 32}
        else:
            pos = {'x': 51, 'y': 32}
    enemy = friend.findNearestEnemy()
    if (friend.health < 29 or (enemy and friend.type == 'archer' and friend.distanceTo(enemy) < 22)):
        self.command(friend, 'move', {'x': 11, 'y': 47})
    elif enemy and friend.distanceTo(enemy) < 20:
        self.command(friend, 'attack', enemy)
    else:
        self.command(friend, 'move', pos)
