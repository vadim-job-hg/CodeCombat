while True:
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if item is not None:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy is not None:
        dist = self.distanceTo(enemy)
        if (enemy.type == 'thrower'):
            self.attack(enemy)
            self.attack(enemy)
        elif (self.isReady("power-up") and (enemy.type == "burl" or enemy.type == "ogre")):
            self.powerUp()
        else:
            if (dist < 15):
                if (self.isReady("cleave") and dist < 15):
                    self.cleave(enemy)
                elif (self.isReady("bash") and dist < 15):
                    self.bash(enemy)
                elif (self.isReady("power-up")):
                    self.powerUp()
                elif (dist > 10):
                    self.attack(enemy)
                    self.attack(enemy)
                else:
                    self.shield()
            else:
                self.shield()
