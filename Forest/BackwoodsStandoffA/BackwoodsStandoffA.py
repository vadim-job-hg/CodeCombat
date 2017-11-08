# https://codecombat.com/play/level/backwoods-standoff-a

while True:  # Use isReady to check if the hero can cleave, otherwise say something!
    enemy = hero.findNearestEnemy();
    if (enemy and hero.isReady('cleave')):
        hero.cleave(enemy)
    else:
        hero.say('DGIGURDA')
