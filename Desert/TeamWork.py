#https://codecombat.com/play/level/team-work
# Should fill in some default source
def commandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'peasant':
            CommandPeasant(friend)


def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        self.command(soldier, "move", item.pos)


while True:
    commandTroops()
    hero.move({'x': 41, 'y': 55})
