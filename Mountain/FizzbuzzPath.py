# https://codecombat.com/play/level/fizzbuzz-path
# Будь внимателен к спрятанным ловушкам и считай свои шаги
# Монеты делятся каждые десять метров

steps = 1

while True:
    # Если количество шагов делится на 3 -- двигайся на Восток
    if steps % 3 == 0 and steps % 5 != 0:
        hero.moveXY(hero.pos.x + 10, hero.pos.y)
    # Если количество шагов делится на 5 -- двигайся на Запад
    elif steps % 3 != 0 and steps % 5 == 0:
        hero.moveXY(hero.pos.x - 10, hero.pos.y)
    # Если количество шагов делится и на 3, и на 5 -- двигайся на Северо-Запад
    elif steps % 3 == 0 and steps % 5 == 0:
        hero.moveXY(hero.pos.x - 10, hero.pos.y + 10)
    # Иначе иди на Север
    else:
        hero.moveXY(hero.pos.x, hero.pos.y + 10)

    steps += 1
