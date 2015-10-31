loop:
    enemys = self.findEnemies()
    index = 0
    closest_soldier = None
    soldier_dist = 999    
    closest_archer = None
    archer_dist = 999
    closest = None
    dist = 999
    close_count = 0;
    priority = None
    while(index<len(enemys)):  
        distance = self.distanceTo(enemys[index])
        shield = False;
        if(enemys[index].type == 'shaman' and distance<20):
            priority = enemys[index];
        if(enemys[index].type == 'Ogre' and distance<10):
            shield = True
        if(distance<10):
            close_count +=1
        if(enemys[index].health>0):
            if(enemys[index].type == 'archer' and distance<archer_dist):
                archer_dist=distance
                closest_archer = enemys[index]
            if(enemys[index].type == 'soldier' and distance<soldier_dist):
                soldier_dist=distance
                closest_soldier = enemys[index] 
            if(distance<dist):
                soldier_dist=dist
                closest = enemys[index]
        index +=1
    if(priority):
        enemy = priority
#    elif(closest_archer and archer_dist<15):
#        enemy = closest_archer
#    elif(closest_soldier and soldier_dist<10):
#        enemy = closest_soldier
    else:
        enemy = closest
    if(self.health<self.maxHealth/3):
        item = self.findNearest(self.findItems())
        if(item):
            if(self.isReady("jump")):
                self.jumpTo(item.pos)
            else:
                self.move(item.pos)
    elif(enemy):
        if(self.isReady("jump") and self.distanceTo>10):
            self.jumpTo(enemy.pos)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif(self.isReady("cleave") and close_count>=7):
            self.cleave(enemy)
        elif(shield):
            self.shield()
        elif(close_count<10 or priority):
            self.attack(enemy)
        else:
            self.shield()
