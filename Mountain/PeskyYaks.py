# https://codecombat.com/play/level/pesky-yaks
# Целое стадо яков!
# Если ты планируешь выжить, то научись фильтровать яков...
def removeByType(enemies, excludedType):
    tempList = []
    # Проверь тип каждого врага, не равен ли он `excludedType`.
    for enemy in enemies:
        # Если нет, добавь (`append`) к списку.
        if enemy.type != excludedType:
            tempList.append(enemy)
        pass
    return tempList


while True:
    # Найди врагов!
    enemies = hero.findEnemies()
    # Убери этих противных яков.
    enemies = removeByType(enemies, "sand-yak")
    enemy = hero.findNearest(enemies)
    if enemy:
        # Теперь... убери (`remove`) тех врагов.
        hero.attack(enemy)

