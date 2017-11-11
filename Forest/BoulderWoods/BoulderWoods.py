# http://codecombat.com/play/level/boulder-woods
# При помощи isPathClear обойди хаотично расставленные валуны.
# Автоматический поиск пути не работает на этом уровне.
while True:
    angle = Math.PI / 2 - Math.PI / 16
    while angle >= -Math.PI / 2:
        targetX = hero.pos.x + 5 * Math.cos(angle)
        targetY = hero.pos.y + 5 * Math.sin(angle)
        # Используй isPathClear для проверки 
        # Если путь свободен, двигайся к цели.
        if (hero.isPathClear(hero.pos, {'x': targetX, 'y': targetY})):
            hero.moveXY(targetX, targetY)
        else:
            # В противном случае немного повернись по часовой стрелке.
            angle -= Math.PI / 16
