path = [{'x': 19, 'y': 33}, {'x': 19, 'y': 14}, {'x': 42, 'y': 14}, {'x': 53, 'y': 37}, {'x': 52, 'y': 52}]
index = len(path)
loop:  # Найдите лучника.
friend = self.findNearest(self.findFriends())
enemy = self.findNearest(self.findEnemies())

# Прикажите лучнику атаковать противника.
if friend and enemy:
    if (friend.distanceTo(enemy) > 16):
        self.command(friend, "attack", enemy)
    else:
        self.say(index + '_' + len(path) % index)
        self.command(friend, "move", path[index % len(path)])
if (friend.pos.x == path[index % len(path)].x and friend.pos.y == path[index % len(path)].y):
    index += 1
    # Подождите-ка! Как то не очень получается. Может быть следует попробовать что-нибудь другое?
    # Манчкин ужасно меееедленный...
