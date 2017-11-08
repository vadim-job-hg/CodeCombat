# http://codecombat.com/play/level/mirage-maker
# Если у вас меньше 25 золота, собирайте монетки.
# Далее, постройте приманку, для того чтобы выманить громил.
# Пока у Вашего героя полный уровень здоровья, выкрикивайте оскорбления ограм поменьше, чтобы спровоцировать их.
# Теперь отступайте на свою базу, чтобы устроить им засаду.
def pickUpNearestItem():
    while True:
        items = hero.findItems()
        if (hero.gold < 25):
            nearestItem = hero.findNearest(items)
            if nearestItem:
                hero.moveXY(nearestItem.pos.x, nearestItem.pos.y)
        else:
            break


pickUpNearestItem()
hero.buildXY('decoy', 72, 68)
while True:
    if (hero.health == hero.maxHealth):
        hero.say('waka')
    else:
        hero.moveXY(21, 16)
