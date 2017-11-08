# http://codecombat.com/play/level/ring-bearer
# Для обучения вы должны сопроводить магическое кольцо огромной силы обратно в город
# Фишка в том, чтобы проскользнуть не сражаясь.Много орков прячется в окружающих горах!
# Создайте кольцо из солдат вокруг крестьянина
# Мы дали вам две функции для помощи в этом

# findSoldierOffset возвращает позицию, где солдат должен находиться по отношению к крестьянину.
# Первый аргумент 'soldiers' должен быть массивом твоих солдат
# Второй аргумент 'i'  - индекс солдата(в массиве солдат) для которого вы хотите найти позицию
def findSoldierOffset(soldiers, i):
    soldier = soldiers[i]
    angle = i * 360 / len(soldiers)
    return radialToCartesian(5, angle)


# Функция производит вычисления для определения местоположения солдата
def radialToCartesian(radius, degrees):
    radians = Math.PI / 180 * degrees
    xOffset = radius * Math.cos(radians)
    yOffset = radius * Math.sin(radians)
    return {"x": xOffset, "y": yOffset}


peasant = hero.findByType("peasant")[0]
soldiers = hero.findByType("soldier")
# Используй findByType чтобы сформировать массив из твоих солдат
while True:
    # Используйте for-loop для перебора range(len(soldiers)).
    for index in range(len(soldiers)):
        offset = findSoldierOffset(soldiers, index)
        # Найдите смещение(offset) для солдата
        # hero.say(offset)
        # Добавьте offset.x и offset.y к pos.x и pos.y крестьянина
        x = offset.x + peasant.pos.x
        y = offset.y + peasant.pos.y
        # hero.say(x, y)
        hero.command(soldiers[index], "move", {'x': x, 'y': y})
    # Герой должен поспевать за крестьянином!
    hero.move({"x": hero.pos.x + 0.2, "y": hero.pos.y})
