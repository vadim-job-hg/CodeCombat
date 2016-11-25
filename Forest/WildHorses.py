while True:  # Как Вы можете найти ближайшее союзное существо?
    # horse = ?
    horse = hero.findNearest(hero.findFriends())
    if horse:
        x1 = horse.pos.x - 7
        x2 = horse.pos.x + 7
        y = horse.pos.y
        if x1 >= 1:
            hero.moveXY(x1, y)
        elif x2 <= 79:
            hero.moveXY(x2, y)
        horse = hero.findNearest(hero.findFriends())
        distance = hero.distanceTo(horse)
        if distance <= 10:
            hero.say("Whoa")
            # Идите к красному кресту, чтобы вернуть лошадь в стойло.
            hero.moveXY(27, 54)
            # Снова возвращайтесь на пастбище и поищите следующую лошадь.
