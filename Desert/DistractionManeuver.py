# https://codecombat.com/play/level/distraction-maneuver
# Защити крестьян!

# Эта функция определяет дальний юнит.
def findFurthest(units):
    furthestUnit = None
    maxDistance = 0
    unitIndex = 0
    while unitIndex < len(units):
        currentUnit = units[unitIndex]
        # Найди расстояние до `currentUnit`:
        distance = hero.distanceTo(currentUnit)
        # Если это расстояние больше, чем `maxDistance`:
        if distance > maxDistance:
            # Переназначь `furthestUnit` и `maxDistance`:
            furthestUnit = currentUnit
            maxDistance = distance

        unitIndex += 1
    return furthestUnit


# Как `findNearestEnemy`, только наоборот.
def findFurthestEnemy():
    enemies = hero.findEnemies()
    furthestEnemy = findFurthest(enemies)
    # Return furthestEnemy:
    return furthestEnemy


# В этой функции герой атакует, не отвлекаясь.
def attackWhileAlive(target):
    # Атакуй цель (`target`), пока её здоровье (`health`) > 0:
    while target.health > 0:
        hero.attack(target)
    pass


while True:
    # Чтобы защитить крестьян, охоться на дальних огров.
    furthestOgre = findFurthestEnemy()
    if furthestOgre:
        attackWhileAlive(furthestOgre)
