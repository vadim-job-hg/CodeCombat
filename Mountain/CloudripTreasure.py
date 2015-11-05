# Цель - собирать монеты / самоцветы.
# Этот уровень повторяемый. Если ты выиграешь, сложность и награда возрастут.
# Если ты проиграешь, придется подождать сутки до следующей попытки.
# Это дополнительное испытание. Его не обязательно проходить для продолжения кампании.
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")


# commands attack
def commandSoldiers():
    for soldier in self.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            self.command(soldier, "attack", enemy)
middleX = 76
middleY = 61
loop:
    summonSoldier()
    commandSoldiers()
    enemy = self.findNearest(self.findEnemies())
    item = self.findNearest(self.findItems())
    flag = self.findFlag()
    if(enemy):
        dist = self.distanceTo(enemy);
    if (enemy and dist<30):
        if(self.isReady("cleave")):
            self.cleave(enemy)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        else:
            self.attack(enemy)
    elif(item):
        self.move(item.pos)
    elif(True):
        self.moveXY(middleX, middleY)
