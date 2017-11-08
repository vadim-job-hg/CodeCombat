# http://codecombat.com/play/level/bookkeeper
def attack(target):
    if target:
        if (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)


eCount = 0
iCount = 0
hero.wait(1)
while True:  # enemy = hero.findNearestEnemy()
    enemy = hero.findNearestEnemy()
    # item  = hero.findNearestItem()
    item = hero.findNearestItem()
    if (enemy):
        attack(enemy)
        attack(enemy)
        eCount = eCount + 1
        iCount = 0
        hero.wait(1)
    elif (item and hero.now() <= 30):
        hero.moveXY(item.pos.x, item.pos.y)
        iCount = hero.gold
        eCount = 0
    else:
        hero.moveXY(59, 33)
        if (eCount > 0 or iCount > 0):
            hero.say(eCount + iCount)
