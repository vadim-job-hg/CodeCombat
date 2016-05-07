#http://codecombat.com/play/level/arcane-ally
def attack(target):
    if target:
        if(self.distanceTo(target)>10):
            self.move(target.pos)
        elif(self.isReady("bash")):
            self.bash(target)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(target)
        elif(self.isReady("cleave")):
            self.cleave(target)
        elif(self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        else:
            self.attack(target)
            self.shield()
loop:
    enemy = hero.findNearest(hero.findEnemies())
    attack(enemy)
