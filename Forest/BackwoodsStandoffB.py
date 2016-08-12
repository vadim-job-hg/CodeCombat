# https://codecombat.com/play/level/backwoods-standoff-b

while True:  # Use isReady to check if the hero can cleave, otherwise say something!
    enemy = self.findNearestEnemy();
    if (enemy and self.isReady('cleave')):
        self.cleave(enemy)
    else:
        self.say('DGIGURDA')
