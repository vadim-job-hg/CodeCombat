# Достигни конца лабиринта, используя команды перемещения.
# Подсчитай количество подобранных самоцветов и скажи это количество рядом с огненной ловушкой, чтобы отключить её.
# Ворон на старте выдаст тебе пароль. Скажи пароль рядом с дверью, чтобы открыть её.
# Убей огров, рядом с которыми окажешься.
# Ты можешь использовать цикл 'loop' для повтора инструкций, если необходимо.
# Если ты пройдёшь этот уровень, то сможешь перейти в Лес Темнодрев!
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
    
