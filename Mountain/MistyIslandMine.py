# https://codecombat.com/play/level/misty-island-mine
# Командуй крестьянами мудро, чтобы эффективно собирать золото.
# Крестьяне должны собирать монеты и строить приманки.

# Функция должна вернуть лучший предмет для прицеливания
# Используй массив из `id`, чтобы 2 крестьянина не шли за одним предметом.
def findBestItem(friend, excludedItems):
    items = friend.findItems()
    bestItem = None
    bestItemValue = 0
    for item in items:
        # Используй `in` для проверки вхождения элемента в массив `excludedItems`.
        # В этом случае пропусти предмет, другой крестьянин уже нацелился на него.
        if item not in excludedItems:
            if bestItemValue < item.value / friend.distanceTo(item):
                bestItemValue = item.value / friend.distanceTo(item)
                bestItem = item
                # Закончи функцию!
                # Помни, что `bestItemValue` должно вычисляться как максимальное `item.value / distanceTo`
    return bestItem


while True:
    peasants = hero.findByType("peasant")
    # Создавай новый массив в каждом цикле.
    claimedItems = []
    for peasant in peasants:
        enemy = peasant.findNearestEnemy()
        if enemy:
            # If the peasant is the target of the enemy
            # И у героя достаточно золота на приманку
            if hero.gold > hero.costOf('decoy'):
                # Прикажи крестьянину строить приманку:
                hero.command(peasant, 'buildXY', 'decoy', peasant.pos.x, peasant.pos.y)
                # Добавь `continue`, чтобы крестьянин не собирал монеты во время стройки.
                continue
            pass
        item = findBestItem(peasant, claimedItems)
        if item:
            # hero.say(item.pos.x)
            # После получение предмета помести его в массив `claimedItems`.
            claimedItems.append(item)
            # Прикажи крестьянину собрать монету:
            hero.command(peasant, 'move', item.pos)

