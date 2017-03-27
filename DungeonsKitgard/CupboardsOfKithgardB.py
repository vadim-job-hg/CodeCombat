# https://codecombat.com/play/level/cupboards-of-kithgard-b
# Поблизости может быть что-то, что поможет тебе.

# Сначала двигайся к Шкафу.
hero.moveRight()
hero.moveDown()
hero.moveRight()
hero.moveDown()
hero.moveDown()
# Потом атакуй Шкаф ( "Cupboard" ) с использованием цикла.
while True:
    hero.attack("Cupboard")
