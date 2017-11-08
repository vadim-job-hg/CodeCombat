# https://codecombat.com/play/level/dance-off
# Двигайся синхронно с партнёром, чтобы впечатлить Пендер Проклинательницу.
friend = hero.findNearest(hero.findFriends())
diffx = friend.pos.x - hero.pos.x
diffy = friend.pos.y - hero.pos.y
while True:
    target = {'x': friend.pos.x - diffx, 'y': friend.pos.y - diffy}
    hero.move(target)
