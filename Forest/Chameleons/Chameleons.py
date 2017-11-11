# https://codecombat.com/play/level/chameleons
# Ogres are disguised as gems or coins.

while True:
    enemy = hero.findNearestEnemy()
    # If you see an enemy - attack it.
    if enemy:
        hero.attack(enemy)
    item = hero.findNearestItem()
    # If you see an item - try to collect it.
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
