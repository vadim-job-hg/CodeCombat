def barkForMaster(event):
    if event.speaker == hero:
        pet.say("WOOF")

pet.on("hear", barkForMaster)

while True:
    enemies = hero.findEnemies()
    if(len(enemies)>0):
        hero.say('WOOF')
        if(hero.isReady('jump')):
            hero.jumpTo({'x':30, 'y':33})
        else:
            hero.moveXY(30, 33)
        hero.moveXY(30, 15)
