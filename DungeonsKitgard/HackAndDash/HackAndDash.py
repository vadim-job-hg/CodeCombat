# http://codecombat.com/play/level/hack-and-dash
# Вы можете написать код перед петлей ('loop')
# Сломайте "Сундук" перед использование команды loop чтобы покинуть лабиринт!
hero.moveRight()
hero.moveUp()
hero.attack('Chest')
hero.moveDown()
while True:
    # Сделайте 3 хода.
    hero.moveRight(3)
    hero.moveDown(3)
