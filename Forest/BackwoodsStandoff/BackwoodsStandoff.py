# These Munchkins are scared of the hero!
# Say something and they'll back off.
# However, once there are enough Munchkins, they will gang up and ambush! Be careful!
# Whenever you can, cleave to clear the mass of enemies.

while True:  # Use isReady to check if the hero can cleave, otherwise say something!
    enemies = hero.findEnemies();
    enemy = hero.findNearest(enemies);
    if (enemy and hero.isReady('cleave')):
        hero.cleave(enemy)
    else:
        hero.say('DGIGURDA')
