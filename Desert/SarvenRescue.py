#https://codecombat.com/play/level/sarven-rescue
# Спаси крестьянку от бандитов и верни её в её деревню.
# Выбери решение, которое тебе подходит:избегай патруль или двигайся прямо на них
# Зелье даёт случайный эффект:как хороший, так и плохой.
# Очень храбрый ? Бонус, если украдешь у огра сундук с сокровищами
array = [[3, 35], [72, 36], [71, 52], [119,29],[130, 106],[27, 106]]
arrayIndex = 0;
while arrayIndex < len(array):
    enemy = self.findNearest(self.findEnemies())
    item = self.findNearest(self.findItems())
    if (enemy and self.distanceTo(enemy) < 50):
        if (self.isReady('jump') and self.distanceTo(enemy) > 10):
            self.jumpTo(enemy.pos)
        elif (self.isReady("cleave")):
            self.cleave(enemy)
        elif (self.isReady("bash")):
            self.bash(enemy)
        elif (self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        else:
            self.attack(enemy)
    elif (item and hero.distanceTo(item)<40):
        if (self.isReady('jump')):
            self.jumpTo(item.pos)
        else:
            self.move(item.pos)
    else:
        if (self.isReady('jump')):
            self.jumpTo({'x': array[arrayIndex][0], 'y': array[arrayIndex][1]})
        else:
            self.moveXY(array[arrayIndex][0], array[arrayIndex][1])
        arrayIndex += 1

