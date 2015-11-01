#pickup coin
def pickUpNearestCoin():
    items = self.findItems()
    nearestCoin = self.findNearest(items)
    if nearestCoin:
        self.move(nearestCoin.pos)

# add soldier
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")


# commands attack
def commandSoldiers():
    for soldier in self.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            self.command(soldier, "attack", enemy)

def attack(target):
    if target:
        if(self.isReady("jump") and self.distanceTo>10):
            self.jumpTo(enemy.pos)
        elif(self.isReady("bash")):
            self.bash(enemy)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(enemy)
        elif(self.isReady("cleave")):
            self.cleave(enemy)
        else:
            self.attack(enemy)

def tacktick():
    enemies = self.findEnemies()
    nearest = self.findNearest(enemies)
    friends = self.findFriends()
    if self.distanceTo(nearest)<10:
        attack(nearest)
    elif len(friends)/3<len(enemies):
        attack(nearest)
    else:
        pickUpNearestCoin()