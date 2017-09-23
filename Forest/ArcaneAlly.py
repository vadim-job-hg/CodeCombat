# http://codecombat.com/play/level/arcane-ally
def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            hero.move(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(target)
        elif (hero.isReady("cleave")):
            hero.cleave(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)
            hero.shield()


while True:
    enemy = hero.findNearestEnemy()
    attack(enemy)
