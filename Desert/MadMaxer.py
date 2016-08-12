# Первыми убивай самых дальних врагов.

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = self.findEnemies()

    # Посмотри на всех врагов, чтобы определить, какие из них находятся дальше всех.
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # Разве этот враг не дальше, чем самый дальний враг, которого мы видели вдалеке?
        distance = self.distanceTo(target)
        if distance > maxDistance:
            maxDistance = distance
            farthest = target

    if farthest:
        while farthest.health > 0:
            if (self.isReady("cleave")):
                self.cleave(farthest)
            elif (self.isReady("bash")):
                self.bash(farthest)
            elif (self.isReady("power-up")):
                self.powerUp()
            else:
                self.attack(farthest)
