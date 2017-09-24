# https://codecombat.com/play/level/protect-and-serve?
# Защищай рабочих и животных!

# Обороняй эти две позиции:
defend = []
defend[0] = { "x": 98, "y": 28 }
defend[1] = { "x": 84, "y": 7 }

soldiers = []

friends = hero.findFriends()
for friend in friends:
    if friend.type == "soldier":
        soldiers.append(friend)
    else:
        # Обороняй рабочих:
        defend.append(friend)

while True:
    # Используй цикл `for` для назначения каждому солдату определённой защитной цели
    # Используй `command(soldier, "defend", thang)` или `command(soldier, "defend", position)`
    for i in range(len(soldiers)):
        soldier = soldiers[i]
        self.command(soldier, "defend", defend[i%len(soldiers)])
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
