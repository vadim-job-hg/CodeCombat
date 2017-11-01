center = Vector(40, 35)
punch_array = []
enemies = hero.findEnemies()
friend = hero.findFriends()[0]
ball = self.findNearest(self.findByType('ball'))
ballPoss = Vector(ball.pos.x, ball.pos.y)
for enemy in enemies:
    s2b = Vector.multiply(Vector.normalize(Vector.subtract(ballPoss, enemy.pos)), 7)
    b2p = ball.pos.add(s2b)
    punch_array.append(b2p)

distance = 100
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