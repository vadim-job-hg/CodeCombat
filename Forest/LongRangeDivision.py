# http://codecombat.com/play/level/long-range-division
# Уничтожьте мины!
# Use say to call out the range to the mines.
# Используйте деление для вычисления дальности.

enemy = hero.findNearestEnemy()
distanceToEnemy = hero.distanceTo(enemy)
# Say first Range: distanceToEnemy divided by 3
hero.say(distanceToEnemy / 3)
hero.say("Огонь!")
# Say second range: distanceToEnemy divided by 1.5
hero.say(distanceToEnemy / 1.5)
hero.say("Огонь!")

# Скажите эти штуки для мотивации. Серьезно. Верьте нам.
hero.say("Йи-ху!")
hero.say("Готово!")
hero.say("Заряд!")

# Теперь используйте while-true цикл для атаки противников.
while True:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
