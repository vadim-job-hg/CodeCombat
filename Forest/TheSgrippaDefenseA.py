#http://codecombat.com/play/level/the-agrippa-defense-a
def cleaveOrAttack(enemy):
    # If "cleave" is ready, cleave; otherwise, attack.
    #enemy = self.findNearestEnemy()
    enemy = self.findNearest(self.findEnemies())
    if(enemy):
        dist = self.distanceTo(enemy)
        if(dist<5):
            if(self.isReady("cleave")):
                self.cleave(enemy)
            else:
                self.attack(enemy)

    pass

while True:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if distance < 5:
            # Call the "cleaveOrAttack" function, defined above.
            cleaveOrAttack(enemy)
