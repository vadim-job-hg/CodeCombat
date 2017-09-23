# https://codecombat.com/play/level/swift-dagger
# Используй лук на дальних дистанциях и кинжал на ближних.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < hero.throwRange:
            # Метни свой кинжал во врага.
            hero.throw(enemy)
        else:
            # Атакуй противника своим луком.
            hero.attack(enemy)

