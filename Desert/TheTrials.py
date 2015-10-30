array = [[60, 22], [76, 22], [127, 24],[90, 24],[127, 24],[76, 22],[60, 22],[76, 22],[60, 22], [34, 21],[12, 55],[11, 75],[11, 110], [58, 125], [91, 131], [112, 119], [91, 131], [57, 122], [39, 92], [78, 75]]
arrayIndex = 0;
while arrayIndex<len(array):
    enemy = self.findNearest(self.findEnemies())
    item = self.findNearest(self.findItems())
    if(enemy and self.distanceTo(enemy)<50):
        if(self.isReady("cleave")):
            self.cleave(enemy)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
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
