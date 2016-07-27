# These Munchkins are scared of the hero!
# Say something and they'll back off.
# However, once there are enough Munchkins, they will gang up and ambush! Be careful!
# Whenever you can, cleave to clear the mass of enemies.

loop:  # Use isReady to check if the hero can cleave, otherwise say something!
enemies = self.findEnemies();
enemy = self.findNearest(enemies);
if (enemy and self.isReady('cleave')):
    self.cleave(enemy)
else:
    self.say('DGIGURDA')
