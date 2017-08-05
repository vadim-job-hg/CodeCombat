# https://codecombat.com/play/level/arrowproof-wolf
# Collect mushrooms.
# First, come to the wolf pet and wake up it (say).
def onHear(b):
    while True:
        m = hero.findEnemyMissiles()
        if len(m) > 0:
            pet.catch(m[0])
        else:
            pet.moveXY(hero.pos.x, hero.pos.y)


hero.moveXY(12, 34)
pet.on('hear', onHear)
hero.say("ВСТАВАЙ, СКОТИНА")
# Next collect mushrooms just usual items.

loop:
item = hero.findNearestItem()
hero.moveXY(item.pos.x, item.pos.y)
