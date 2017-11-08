# Первыми убивай самых дальних врагов.

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Посмотри на всех врагов, чтобы определить, какие из них находятся дальше всех.
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # Разве этот враг не дальше, чем самый дальний враг, которого мы видели вдалеке?
        distance = hero.distanceTo(target)
        if distance > maxDistance:
            maxDistance = distance
            farthest = target

    if farthest:
        while farthest.health > 0:
            if (hero.isReady("cleave")):
                hero.cleave(farthest)
            elif (hero.isReady("bash")):
                hero.bash(farthest)
            elif (hero.isReady("power-up")):
                hero.powerUp()
            else:
                hero.attack(farthest)
