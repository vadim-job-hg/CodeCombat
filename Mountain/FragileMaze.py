#http://codecombat.com/play/level/fragile-maze
distance = 16
move = Vector(0, distance)
rightwall = Vector.rotate(move, -Math.PI/2)
while True:
    direction = Vector.add(move, hero.pos)
    direction2 = Vector.add(rightwall, hero.pos)
    if self.isPathClear(hero.pos, direction2):
        self.moveXY(direction2.x, direction2.y)
        move = rightwall
        rightwall = Vector.rotate(rightwall, -Math.PI/2)
    elif self.isPathClear(hero.pos, direction):
        self.moveXY(direction.x, direction.y)
    else:
        move = Vector.rotate(move, Math.PI/2)
        rightwall = Vector.rotate(rightwall, Math.PI/2)
        direction = Vector.add(move, hero.pos)
        if self.isPathClear(hero.pos, direction):
            self.moveXY(direction.x, direction.y)

