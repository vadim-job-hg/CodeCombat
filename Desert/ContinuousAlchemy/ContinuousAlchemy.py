while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if not enemy:
        continue

    if not item:
        hero.say("Дай мне попить!")
        continue

    if item.type == 'poison':
        continue
    hero.moveXY(item.pos.x, item.pos.y)
    hero.moveXY(34, 48)
