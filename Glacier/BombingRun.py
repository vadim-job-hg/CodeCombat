# http://codecombat.com/play/level/bombing-run

while True:
    enemy = self.findNearestEnemy();
    if enemy:
         # Find the vector of attack
        diff = enemy.pos.subtract(self.pos)
        
        # Say the angle!
        self.say(Vector.heading(diff) * 180 / Math.PI)
        
