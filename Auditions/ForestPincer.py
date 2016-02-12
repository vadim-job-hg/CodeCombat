#http://codecombat.com/play/level/forest-pincer
# Defeat the ogres and live to cross the forest!
# Combine what you've learned about flags with your hero's combat skills.

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    if flag:
        self.pickUpFlag(flag)
    elif enemy:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
