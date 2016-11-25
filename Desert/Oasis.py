# Двигайтесь вперед чтобы достичь оазиса,
# но двигайтесь назад, чтобы избежать яков поблизости.
while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        x = hero.pos.x - 10
        y = hero.pos.y
    else:
        x = hero.pos.x + 10
        y = hero.pos.y
    hero.moveXY(x, y)
