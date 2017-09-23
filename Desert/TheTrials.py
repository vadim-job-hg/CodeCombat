array = [[31, 26], [53, 21], [74, 21], [86, 21], [112, 23], [127, 25], [68, 20], [51, 25], [12, 53], [10, 86],
         [16, 115], [34, 126], [12, 112], [34, 126], [12, 112], [34, 126], [12, 112], [34, 126], [12, 112], [34, 126],
         [12, 112], [44, 130], [60, 125], [85, 32], [103, 125], [85, 32], [103, 125], [85, 32], [103, 125], [85, 32],
         [103, 125], [41, 95], [40, 84], [100, 89], [130, 72], [102, 55]]
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
    elif (item):
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
# Ты должен проложить свой путь к первому испытанию ( Оазис Марр) убивая врагов на протяжении всего пути. Как достигнешь его собери все грибы и испытание начнется. Если переживешь нападение, то держи путь к следующему Оазису за вторым испытанием, а затем - в Храм. Как пройдешь все испытания, ты сразишься с главным боссом. Удачи!
# Подсказка: Очки с высокой дальностью видимости очень помогут вам на этом уровне, поэтому купите лучшее из того, что вы можете получить.
# Подсказка: тип ("type") охранников оазиса 'oasis-guardian'
