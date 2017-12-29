while True:
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    if (enemy and hero.isReady('cleave')):
        hero.cleave(enemy)
    else:
        hero.say('DGIGURDA')
