# http://codecombat.com/play/level/vital-powers
# Этом уровень покажет, как определять собственные функции.
# Код внутри функции не выполняется сразу. Он откладывается на потом.
# Эта функция заставляет вашего героя поднять ближайшую монету.
def pickUpNearestCoin():
    items = self.findItems()
    nearestCoin = self.findNearest(items)
    if nearestCoin and self.distanceTo(nearestCoin) < 30:
        if self.isReady("jump"):
            self.jumpTo(nearestCoin.pos)
        else:
            self.move(nearestCoin.pos)


# С помощью этой функции ваш герой призывает солдата.
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if self.gold > self.costOf("soldier"):
        self.summon("soldier")


# Эта функция приказывает вашим солдатам атаковать ближайшего врага.
def commandSoldiers():
    for soldier in self.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            self.command(soldier, "attack", enemy)


def attack(target):
    if target:
        if (self.isReady("jump") and self.distanceTo > 10):
            self.jumpTo(target.pos)
        elif (self.isReady("bash")):
            self.bash(target)
        elif (self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        else:
            self.attack(target)


def tacktick():
    enemies = self.findEnemies()
    nearest = self.findNearest(enemies)
    friends = self.findFriends()
    if nearest and (self.distanceTo(nearest) < 10 or self.now() > 25):
        attack(nearest)
    elif nearest and len(friends) / 3 < len(enemies):
        attack(nearest)
    else:
        pickUpNearestCoin()


while True:  # В своем цикле ты можешь "вызывать" функции, определенные выше.
    # Эта строка вызывает выполнение кода внутри функции "pickUpNearestCoin" .
    tacktick()
    summonSoldier()
    commandSoldiers()
