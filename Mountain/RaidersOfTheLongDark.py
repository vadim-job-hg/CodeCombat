# https://codecombat.com/play/level/raiders-of-the-long-dark?
# Твоя цель: защитить крестьянина и двигаться вправо.
# Аррин будет защищать спереди и командовать солдатами.
# Тебе нужно прикрывать тыл и командовать крестьянином.

arryn = hero.findByType("raider")[0]
peasant = hero.findByType("peasant")[0]

def chooseHeroStrategy():
    # Верни "fight" или "advance".
    # Вне боя старайся держаться в 5 метрах позади крестьянина.
    # Не удаляйся от крестьянина более чем на 15 метров.
    enemy = peasant.findNearestEnemy()
    if hero.distanceTo(peasant)>15 or not(enemy) or peasant.distanceTo(enemy)>15:
        return "advance"
    else:
        return "fight"
    pass

def heroFight():
    # Останови огров, если они попытаются пробежать мимо тебя к крестьянину!
    # Подсказка: постарайся их замедлить, если получится.
    enemy = peasant.findNearestEnemy()
    if enemy and hero.distanceTo(enemy)<40:
        hero.attack(enemy)
    pass

def heroAdvance():
    # Держись позади крестьянина.
    hero.move(Vector(peasant.pos.x-5,peasant.pos.y))
    pass

def choosePeasantStrategy():
    # Верни "follow", "build-above" или "build-below".
    # Подсказка: Используй функцию `isPathClear()`, чтобы определить местоположение проходов.
    if hero.isPathClear(peasant.pos, Vector(peasant.pos.x, peasant.pos.y+15)):
        return "build-above"
    elif hero.isPathClear(peasant.pos, Vector(peasant.pos.x, peasant.pos.y-15)):
        return "build-below"
    else:
        return "follow"
        
    pass

def peasantAdvance():
    # Держи крестьянина позади Аррин и её солдат.
    hero.command(peasant, 'move', Vector(arryn.pos.x-5,arryn.pos.y))
    pass

def peasantBuild(x,y):
    # Прикажи крестьянину построить частокол.
    hero.command(peasant, 'buildXY', 'palisade', x, y)    

while True:
    heroStrategy = chooseHeroStrategy()
    if heroStrategy == "fight":
        heroFight()
    elif heroStrategy == "advance":
        heroAdvance()
    
    peasantStrategy = choosePeasantStrategy()
    if peasantStrategy == "build-above":
        peasantBuild(peasant.pos.x, peasant.pos.y + 5)
    elif peasantStrategy == "build-below":
        peasantBuild(peasant.pos.x, peasant.pos.y - 5)
    elif peasantStrategy == "follow":
        peasantAdvance()
    
