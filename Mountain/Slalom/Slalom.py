# Используй литералы объектов чтобы пройти безопасным путём и собрать самоцветы.
# Ты не можешь использовать moveXY() на этом уровне! Используй move() чтобы идти куда надо.
gems = hero.findItems()

while hero.pos.x < 20:
    hero.move({'x': 20, 'y': 35})
while hero.pos.x < 25:
    gem0 = gems[0]
    hero.move(gem0.pos)
while hero.pos.x < 30:
    hero.move({'x': 30, 'y': 35})
while hero.pos.x < 35:
    gem0 = gems[1]
    hero.move(gem0.pos)
while hero.pos.x < 40:
    hero.move({'x': 40, 'y': 35})
while hero.pos.x < 45:
    gem0 = gems[2]
    hero.move(gem0.pos)
while hero.pos.x < 50:
    hero.move({'x': 50, 'y': 35})
while hero.pos.x < 55:
    gem0 = gems[3]
    hero.move(gem0.pos)
# Когда твой х меньше 30,
# Используй объект чтобы идти к 30, 35.

# Когда твой х меньше чем 35,
# Иди к позиции gems[1].

# Get to the last couple of gems yourself!
