# todo:
i = 1;
loop:
self.moveRight()
self.moveUp()
self.moveUp()
enemy = self.findNearestEnemy()
if enemy:
    self.attack(enemy)
    self.attack(enemy)
self.moveLeft()
self.moveUp()
self.moveUp()
self.moveRight()
self.moveRight()
self.moveUp()
self.moveDown()
self.moveRight()
self.moveDown()
self.moveDown()
self.say(i)
self.moveDown()
self.moveDown()
self.say('Abracadabra')
self.moveRight()
self.moveRight()
i = i + 1
