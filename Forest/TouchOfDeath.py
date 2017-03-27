# https://codecombat.com/play/level/touch-of-death
# Накладывай заклинание "drain-life" на короткой дистанции.
# Используй посох для атаки на расстоянии.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 15:
            # Наложи заклинание "drain-life" на врага.
            hero.cast("drain-life", enemy)
        else:
            # Атакуй врага при помощи посоха.
            hero.attack(enemy)

