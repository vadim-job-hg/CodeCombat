goalPoint = Vector(78, 34)
while True:
    goal = Vector.subtract(goalPoint, hero.pos)
    goal = Vector.normalize(goal)
    goal = Vector.multiply(goal, 10)
    yak = hero.findNearestEnemy()
    distance = hero.distanceTo(yak)
    if distance < 10:
        yak_vector = Vector.subtract(hero.pos, yak.pos)
        yak_vector = Vector.normalize(yak_vector)
        yak_vector = Vector.multiply(yak_vector, 10)
        goal = Vector.add(yak_vector, goal)
    moveToPos = Vector.add(hero.pos, goal)
    hero.move(moveToPos)
