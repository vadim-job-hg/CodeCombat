# Попросите целителя о помощи, если у вас осталось меньше одной третьей здоровья.
while True:
    currentHealth = self.health
    healingThreshold = self.maxHealth / 4
    # Если ваше текущее здоровье меньше уровня,
    # перейдите к точке исцеления и скажите: "heal me".
    # Иначе, атакуйте. Вам надо будет бороться изо всех сил!
    if (currentHealth < healingThreshold):
        self.moveXY(65, 45)
        self.say('heal me')
    else:
        enemy = self.findNearestEnemy()
        if enemy:
            if (self.isReady("cleave")):
                self.cleave(enemy)
            elif (self.isReady("bash")):
                self.bash(enemy)
            elif (self.isReady("power-up")):
                self.powerUp()
            else:
                self.attack(enemy)
