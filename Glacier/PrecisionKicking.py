# https://codecombat.com/play/level/precision-kicking
# Стукай по мячу так, чтобы перебить всех синих скелетов, не трогая красных.
# Синие скелеты могут быть найдены как враги.
center = Vector(40, 35)
punch_array = []
enemies = hero.findEnemies()
friend = hero.findFriends()[0]
ball = self.findNearest(self.findByType('ball'))
ballPoss = Vector(ball.pos.x, ball.pos.y)
for enemy in enemies:
    # step 1 vector from skeleton to ball
    s2b = Vector.multiply(Vector.normalize(Vector.subtract(ballPoss, enemy.pos)), 7)
    # step 2 vector from ball to target position
    b2p = ball.pos.add(s2b)
    # step 3 vector from ball to current position
    # b2u = Vector.multiply(Vector.normalize(Vector.subtract(friend.pos, ballPoss)), 7)
    # while friend.distanceTo(b2p)>1:
    #    hero.command(friend, 'move', ball.pos.add(b2u))
    #    b2u = Vector.rotate(b2u, Math.PI/30)
    #    hero.wait(0.2)
    # hero.wait(1)
    # cur = Vector(friend.pos.x, friend.pos.y)
    # hero.command(friend, 'move', ball.pos)
    # hero.wait(1)
    punch_array.append(b2p)

distance = 100
# sorted(punch_array, key=lambda item: item[1], reverse=False)
while len(punch_array) > 0:
    min_dist, min_index = 999, -1
    for index, punch in enumerate(punch_array):
        if min_dist > Vector.subtract(punch, friend.pos).magnitude():
            min_dist = Vector.subtract(punch, friend.pos).magnitude()
            min_index = index
    vector = punch_array.pop(min_index)
    hero.command(friend, 'move', vector)
    hero.wait(1)
    hero.command(friend, 'move', center)
    hero.wait(1)
    hero.command(friend, 'move', vector)
    # hero.say(punch_array[0])