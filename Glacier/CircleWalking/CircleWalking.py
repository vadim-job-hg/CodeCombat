center = Vector(40, 34)
partner = hero.findByType("peasant")[0]
while True:
    vector = Vector.subtract(partner.pos, center)
    moveToPos = Vector.subtract(center, vector)
    hero.move(moveToPos)
