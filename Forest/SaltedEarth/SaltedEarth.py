while True:
    enemy = hero.findNearestEnemy()
    if enemy.type == "munchkin" or enemy.type == "thrower":
        hero.attack(enemy)
    item = hero.findNearestItem()
    if (item.type == 'gem' or item.type == 'coin'):
        itemPosition=item.pos
        itemX = itemPosition.x
        itemY = itemPosition.y
        hero.moveXY(itemX, itemY)
