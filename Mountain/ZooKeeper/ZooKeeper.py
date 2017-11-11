# Защити клетку.
# Поставь солдата на каждый Х.
points = []
points[0] = {"x": 33, "y": 42}
points[1] = {"x": 47, "y": 42}
points[2] = {"x": 33, "y": 26}
points[3] = {"x": 47, "y": 26}
# Собери 80 золота.
while hero.gold < 80:
    item = hero.findNearestItem()
    if (item):
        if (hero.isReady("jump")):
            hero.jumpTo({'x': item.pos.x, 'y': item.pos.y})
        else:
            hero.move(item.pos)
# Призови четырех солдат.
for i in range(4):
    hero.summon("soldier")

# Отправь своих солдат на позиции.
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            # Прикажи войскам атаковать.
            hero.command(friend, 'attack', enemy)
        else:
            hero.command(friend, 'move', point)
