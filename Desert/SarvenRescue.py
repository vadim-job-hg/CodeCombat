# https://codecombat.com/play/level/sarven-rescue
# Спаси крестьянку от бандитов и верни её в её деревню.
# Выбери решение, которое тебе подходит:избегай патруль или двигайся прямо на них
# Зелье даёт случайный эффект:как хороший, так и плохой.
# Очень храбрый ? Бонус, если украдешь у огра сундук с сокровищами
array = [[3, 35], [72, 36], [71, 52], [119,29],[130, 106],[27, 106]]
arrayIndex = 0;
while arrayIndex < len(array):
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if (enemy and hero.distanceTo(enemy) < 50):
        if (hero.isReady('jump') and hero.distanceTo(enemy) > 10):
            hero.jumpTo(enemy.pos)
        elif (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        else:
            hero.attack(enemy)
    elif (item and hero.distanceTo(item)<40):
        if (hero.isReady('jump')):
            hero.jumpTo(item.pos)
        else:
            hero.move(item.pos)
    else:
        if (hero.isReady('jump')):
            hero.jumpTo({'x': array[arrayIndex][0], 'y': array[arrayIndex][1]})
        else:
            hero.moveXY(array[arrayIndex][0], array[arrayIndex][1])
        arrayIndex += 1

