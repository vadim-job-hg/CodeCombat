# http://codecombat.com/play/level/bombing-run

# Incoming oscars! (That's military speak for ogres).
# You will need to calculate their angle of attack.
# Use that angle to command your Griffin Bombers!

while True:
    enemy = self.findNearestEnemy();
    if enemy:
         # Find the vector of attack
        #diff = enemy.pos.subtract(self.pos)
        vector = Math.atan2(enemy.pos.y, enemy.pos.x)
        vector = vector * 180 / Math.PI+30
        # Say the angle!
        self.say(vector)
        
