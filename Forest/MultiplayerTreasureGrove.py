while True:
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    dist_item = 9999999
    dist_enemy = 99999999
    if item:
        dist_item = self.distanceTo(item)
    if enemy:
        dist_enemy = self.distanceTo(enemy)
    if ((dist_enemy < 10) or (dist_item > dist_enemy)):
        if (self.isReady("cleave")):
            self.cleave(enemy)
        elif (self.isReady("bash")):
            self.bash(enemy)
        elif (self.isReady("power-up")):
            self.powerUp()
        else:
            self.shield()
            self.attack(enemy)
    elif (item):
        self.moveXY(item.pos.x, item.pos.y)
    else:
        self.moveXY(42, 30)
