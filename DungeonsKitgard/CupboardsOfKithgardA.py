# https://codecombat.com/play/level/cupboards-of-kithgard-a
# Поблизости может быть что-то, что поможет тебе.

# Сначала двигайся к Шкафу.
hero.moveDown()
hero.moveLeft()
hero.moveLeft()
hero.moveUp()
hero.moveUp()
# Потом атакуй Шкаф ( "Cupboard" ) с использованием цикла.
while True:
    hero.attack("Cupboard")
