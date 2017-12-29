while True:
    enemy = hero.findNearestEnemy()
    if (enemy and hero.isReady('cleave')):
        hero.cleave(enemy)
    else:
        hero.say('DGIGURDA')
