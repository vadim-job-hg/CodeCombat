# https://codecombat.com/play/level/the-dunes
# Соберите монеты. Игнорируйте яков и бурлей. Сражайтесь с метателями и ограми.
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if enemy.type is "sand-yak" or enemy.type is "burl":
            # Не сражайтесь с яками и бурлями! Просто продолжайте собирать монеты.
            item = hero.findNearestItem()
            if item:
                hero.move(item.pos)
            pass
        else:
            # Но если тип врага "thrower" или "ogre", атакуйте их.
            if enemy.type is "thrower" or enemy.type is "ogre":
                hero.attack(enemy)

    elif item:
        # Собирайте монеты
        item = hero.findNearestItem()
        if item:
            hero.move(item.pos)
        pass
