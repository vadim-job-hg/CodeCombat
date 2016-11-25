# Попросите целителя о помощи, если у вас осталось меньше одной третьей здоровья.
while True:
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 4
    # Если ваше текущее здоровье меньше уровня,
    # перейдите к точке исцеления и скажите: "heal me".
    # Иначе, атакуйте. Вам надо будет бороться изо всех сил!
    if (currentHealth < healingThreshold):
        hero.moveXY(65, 45)
        hero.say('heal me')
    else:
        enemy = hero.findNearestEnemy()
        if enemy:
            if (hero.isReady("cleave")):
                hero.cleave(enemy)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            elif (hero.isReady("power-up")):
                hero.powerUp()
            else:
                hero.attack(enemy)
