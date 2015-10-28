loop:
   enemy =  self.findNearestEnemy()
   dist = self.distanceTo(enemy)
   if(dist<10):
       self.cleave(enemy)    
   else:
       self.attack("Chest")