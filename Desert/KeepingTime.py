# Используйте свои новые навыки, чтобы выбрать что делать: self.now()

loop:  # Если это первые 10 секунд, сражайтесь.
if self.now() < 10 or self.now() > 30:
    enemy = self.findNearestEnemy()
    if enemy:
        if (self.health < self.maxHealth / 4):
            self.moveXY(21, 52)
        elif (self.isReady("cleave")):
            self.cleave(enemy)
        elif (self.isReady("bash")):
            self.bash(enemy)
        elif (self.isReady("power-up")):
            self.powerUp()
        else:
            self.attack(enemy)
elif self.now() <= 30:
    item = self.findNearestItem()
    if (item):
        moveToX = item.pos.x
        moveToY = item.pos.y
        self.moveXY(moveToX, moveToY)
        # Иначе, если это первые 30 секунд, собирайте монеты.
        # После 30-ой секунды, присоединяйтесь к остальным!
