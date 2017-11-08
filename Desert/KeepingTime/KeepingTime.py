# Используйте свои новые навыки, чтобы выбрать что делать: hero.now()

while True:  # Если это первые 10 секунд, сражайтесь.
    if hero.now() < 10 or hero.now() > 30:
        enemy = hero.findNearestEnemy()
        if enemy:
            if (hero.health < hero.maxHealth / 4):
                hero.moveXY(21, 52)
            elif (hero.isReady("cleave")):
                hero.cleave(enemy)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            elif (hero.isReady("power-up")):
                hero.powerUp()
            else:
                hero.attack(enemy)
    elif hero.now() <= 30:
        item = hero.findNearestItem()
        if (item):
            moveToX = item.pos.x
            moveToY = item.pos.y
            hero.moveXY(moveToX, moveToY)
            # Иначе, если это первые 30 секунд, собирайте монеты.
            # После 30-ой секунды, присоединяйтесь к остальным!
