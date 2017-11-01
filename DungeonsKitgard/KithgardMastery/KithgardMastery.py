i = 0
while True:    
    self.moveUp()
    self.moveRight(3)
    self.moveUp()
    i = i + 1
    self.moveDown()
    self.moveRight()
    self.say('Swordfish')
    self.moveRight(2)
    self.moveUp()
    hero.say(i)
    self.moveUp(2)
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
    self.moveLeft(4)
    self.moveUp(2)
    
