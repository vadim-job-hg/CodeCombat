# Иди к оазису. Опасайся новых врагов: огров-скаутов!
# Иди по диагонали вправо-вверх, увеличивая текущие X и Y координаты.
loop:
    # Атакуй любого врага на пути или продолжай идти.
    enemy = self.findNearestEnemy()
    if enemy:
        if(self.isReady("cleave")):
            self.cleave(enemy)
         elif(self.isReady("bash")):
            self.bash(enemy)
         elif(self.isReady("power-up")):
            self.powerUp()
         else:
            self.attack(enemy)
    else:
        x = self.pos.x + 10
        y = self.pos.y + 10
        self.moveXY(x, y)
