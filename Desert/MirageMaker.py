#http://codecombat.com/play/level/mirage-maker
# Если у вас меньше 25 золота, собирайте монетки.
# Далее, постройте приманку, для того чтобы выманить громил.
# Пока у Вашего героя полный уровень здоровья, выкрикивайте оскорбления ограм поменьше, чтобы спровоцировать их.
# Теперь отступайте на свою базу, чтобы устроить им засаду.
def pickUpNearestItem():
    loop:
        items = self.findItems()
        if(self.gold<25):
            nearestItem = self.findNearest(items)
            if nearestItem:
                self.moveXY(nearestItem.pos.x, nearestItem.pos.y)
        else:
            break;
pickUpNearestItem()
self.buildXY('decoy', 72, 68)
loop:
    if(self.health==self.maxHealth):
        self.say('waka')
    else:
        self.moveXY(21, 16)



