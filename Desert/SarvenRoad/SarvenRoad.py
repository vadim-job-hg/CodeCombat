# Иди к оазису. Опасайся новых врагов: огров-скаутов!
# Иди по диагонали вправо-вверх, увеличивая текущие X и Y координаты.
while True:  # Атакуй любого врага на пути или продолжай идти.
    enemy = hero.findNearestEnemy()
    if enemy:
        if (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
        else:
            hero.attack(enemy)
    else:
        x = hero.pos.x + 10
        y = hero.pos.y + 10
        hero.moveXY(x, y)
