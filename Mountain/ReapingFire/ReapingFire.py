# http://codecombat.com/play/level/reaping-fire
def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def chooseStrategy():
    enemies = hero.findEnemies()

    # If you can summon a griffin-rider, return "griffin-rider"
    if hero.gold > hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")
    # If there is a fangrider on your side of the mines, return "fight-back"
    fangrider = hero.findByType("fangrider")
    if (len(fangrider) > 0 and fangrider[0].pos.x < 38):
        return "fight-back"
    else:
        return "collect-coins"


def commandAttack():
    # Command your griffin riders to attack ogres.
    pass


def pickUpCoin():
    nearestItem = hero.findNearestItem()
    if nearestItem:
        moveTo(nearestItem.pos)


def heroAttack():
    target = hero.findNearest(hero.findByType("fangrider"))
    if target:
        if (hero.distanceTo(target) < 20):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(target)
        elif (hero.isReady("cleave")):
            hero.cleave(target)
        else:
            hero.attack(target)


def commandTroops():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)


while True:
    commandAttack()
    commandTroops()
    strategy = chooseStrategy()
    if (strategy == "fight-back"):
        heroAttack()
    else:
        pickUpCoin()
