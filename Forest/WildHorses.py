loop:
    # Как Вы можете найти ближайшее союзное существо?
    # horse = ?
    horse = self.findNearest(self.findFriends())    
    if horse:
        x1 = horse.pos.x - 7
        x2 = horse.pos.x + 7
        y  =  horse.pos.y
        if x1 >= 1:
            self.moveXY(x1, y)
        elif x2 <= 79:
            self.moveXY(x2, y)
        horse = self.findNearest(self.findFriends())  
        distance = self.distanceTo(horse)
        if distance <= 10:
            self.say("Whoa")
            # Идите к красному кресту, чтобы вернуть лошадь в стойло.
            self.moveXY(27, 54)
            # Снова возвращайтесь на пастбище и поищите следующую лошадь.
            
            
