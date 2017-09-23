# Собери 80 золота
while hero.gold < 80:
    item = hero.findNearestItem()
    if (item):
        if (hero.isReady("jump")):
            hero.jumpTo({'x': item.pos.x, 'y': item.pos.y})
        else:
            hero.move(item.pos)
# Построй 4 солдата-приманки
for i in range(4):
    hero.summon("soldier")
# Отправь твоих солдат на позиции
points = []
points[0] = {"x": 13, "y": 73}
points[1] = {"x": 51, "y": 73}
points[2] = {"x": 51, "y": 53}
points[3] = {"x": 90, "y": 52}
friends = hero.findFriends()
for j in range(len(friends)):
    point = points[j]
    friend = friends[j]
    enemy = friend.findNearestEnemy()
    hero.command(friend, 'move', point)
# Используйте диапазон множест, чтобы организовать петлю.
# Укажите точки для друзей и прикажите им двигаться к ним
