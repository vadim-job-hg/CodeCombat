# http://codecombat.com/play/level/vital-powers
# Этом уровень покажет, как определять собственные функции.
# Код внутри функции не выполняется сразу. Он откладывается на потом.
# Эта функция заставляет вашего героя поднять ближайшую монету.
def pickUpNearestCoin():
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin and hero.distanceTo(nearestCoin) < 30:
        if hero.isReady("jump"):
            hero.jumpTo(nearestCoin.pos)
        else:
            hero.move(nearestCoin.pos)


# С помощью этой функции ваш герой призывает солдата.
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")


# Эта функция приказывает вашим солдатам атаковать ближайшего врага.
def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)


def attack(target):
    if target:
        if (hero.isReady("jump") and hero.distanceTo > 10):
            hero.jumpTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)


def tacktick():
    enemies = hero.findEnemies()
    nearest = hero.findNearest(enemies)
    friends = hero.findFriends()
    if nearest and (hero.distanceTo(nearest) < 10 or hero.now() > 25):
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
