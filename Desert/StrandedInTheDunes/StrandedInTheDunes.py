# Двигайся к крайней правой стороне карты, чтобы обнаружить новые места.
# Если нужно больше информации, загляни в "Советы".
# https://codecombat.com/play/level/stranded-in-the-dunes
# Иди к крайней правой стороне карты, чтобы обнаружить новые места.
# Смотри инструкцию для уточнения.
def attack(target):
    if target  and target.type!='sand-yak':
        if (hero.distanceTo(target) > 10):
            hero.move(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)
            hero.shield()
#step 1
hero.moveXY(120,39)
while hero.time<100:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type!='sand-yak':
        attack(enemy)
    else:
        hero.move({'x':120, 'y':39})
#step 2
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)
    elif enemy:
        attack(enemy)
    else:
        hero.move({'x':60, 'y':35})
