# https://codecombat.com/play/level/stranded-in-the-dunes
# Иди к крайней правой стороне карты, чтобы обнаружить новые места.
# Смотри инструкцию для уточнения.
def moveTo(position):
    if (hero.isReady("jump")):
        hero.jumpTo(position)
    else:
        hero.move(position)

def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)
            hero.shield()
while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type!='sand-yak':
        attack(enemy)
    else:
        hero.move({'x':hero.pos.x+10, 'y':39})
