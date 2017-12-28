def onHear(b):
    while True:
        m = hero.findEnemyMissiles()
        if len(m) > 0:
            pet.catch(m[0])
        else:
            pet.moveXY(hero.pos.x, hero.pos.y)


hero.moveXY(12, 34)
pet.on('hear', onHear)
hero.say("BOOOOO")
while True:
    item = hero.findNearestItem()
    hero.moveXY(item.pos.x, item.pos.y)
