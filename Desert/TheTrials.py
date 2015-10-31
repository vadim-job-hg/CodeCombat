array = [[31, 26], [53, 21], [74, 21], [86, 21], [112, 23], [127, 25], [68, 20], [51, 25], [12, 53], [10, 86], [16, 115], [34, 126], [12,112], [34, 126], [12,112], [34, 126], [12,112], [34, 126], [12,112], [34, 126],[12,112],[44, 130], [60, 125],[85,32],[103, 125],[85,32],[103, 125],[85,32],[103, 125],[85,32],[103, 125], [41, 95], [40, 84], [100, 89], [130, 72], 102, 55]
arrayIndex = 0;
while arrayIndex<len(array):
    enemy = self.findNearest(self.findEnemies())
    item = self.findNearest(self.findItems())
    if(enemy and self.distanceTo(enemy)<50):
        if(self.isReady('jump') and self.distanceTo(enemy)>10):
            self.jumpTo(enemy.pos)
        elif(self.isReady("cleave")):
            self.cleave(enemy)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        else:
            self.attack(enemy)
    elif(item):
        if(self.isReady('jump')):
            self.jumpTo(item.pos)
        else:
            self.move(item.pos)
    else:
        if(self.isReady('jump')):
            self.jumpTo({'x':array[arrayIndex][0], 'y':array[arrayIndex][1]})
        else:
            self.moveXY(array[arrayIndex][0], array[arrayIndex][1])
        arrayIndex += 1
# Ты должен проложить свой путь к первому испытанию ( Оазис Марр) убивая врагов на протяжении всего пути. Как достигнешь его собери все грибы и испытание начнется. Если переживешь нападение, то держи путь к следующему Оазису за вторым испытанием, а затем - в Храм. Как пройдешь все испытания, ты сразишься с главным боссом. Удачи!
# Подсказка: Очки с высокой дальностью видимости очень помогут вам на этом уровне, поэтому купите лучшее из того, что вы можете получить.
# Подсказка: тип ("type") охранников оазиса 'oasis-guardian'
