# http://codecombat.com/play/level/odd-sandstorm
# Этот массив содержит и друзей, и огров.
# Чётные элементы - огры, нечётные - друзья.
everybody = ['Yetu', 'Tabitha', 'Rasha', 'Max', 'Yazul', 'Todd']
enemyIndex = 0

while enemyIndex < len(everybody):
    # Используйте квадратные скобки, чтобы получить имя огра из массива.
    if (everybody[enemyIndex]):
        # Атакуйте, используя переменную с именем огра.
        hero.attack(everybody[enemyIndex])
    # Увеличивай индекс на 2, чтобы перебрать друзей.
    enemyIndex += 2
hero.moveXY(36, 54)
# После уничтожения огров двигайся к оазису.
