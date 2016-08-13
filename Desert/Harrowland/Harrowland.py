# http://codecombat.com/play/level/harrowland
while True:
    enemy = None
    dist = 99999
    enemys = self.findEnemies()
    index = 0
    while (index < len(enemys)):
        distance = self.distanceTo(enemys[index])
        if (enemys[index].health > 0 and enemys[index].type != "sand-yak"):
            if (distance < dist):
                dist = distance
                enemy = enemys[index]
        index += 1
    if (enemy):
        if (self.isReady("jump") and self.distanceTo > 15):
            self.jumpTo(enemy.pos)
        elif (self.isReady("bash")):
            self.bash(enemy)
        elif (self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif (self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.attack(enemy)
