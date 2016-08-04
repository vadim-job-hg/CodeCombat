# http://codecombat.com/play/level/fragile-maze
distance = 16
move = Vector(distance, 0)
direction = Vector.add(move, hero.pos)
while True:
    while not (self.isPathClear(hero.pos, direction)):
        move = Vector.rotate(move, Math.PI / 2)
        direction = Vector.add(move, hero.pos)
        # hero.say(direction)
    self.moveXY(direction.x, direction.y)
    move = Vector.rotate(move, -Math.PI / 2)
    direction = Vector.add(move, hero.pos)