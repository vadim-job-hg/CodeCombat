loop:
    enemys = self.findEnemies()
    index = 0
    while(index<len(enemys)):        
        index +=1
        if(enemys[index] and enemys[index].type == 'archer'):
            if(self.isReady("bash")):
                self.bash(enemys[index])
            elif(self.isReady("power-up")):
                self.powerUp()
                self.attack(enemys[index])
            elif(self.isReady("cleave")):
                self.cleave(enemys[index])
            else:
                self.shield(enemys[index])
