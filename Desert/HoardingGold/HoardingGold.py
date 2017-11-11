# Собери 25 золота и назови Нарии сумму.
# Используй "breake", чтобы остановить сбор, когда totalGold >= 25.
totalGold = 0
while True:
    coin = hero.findNearestItem()
    # Pick up the coin.
    hero.moveXY(coin.pos.x, coin.pos.y)
    # Add the coin's value to totalGold. (See the guide for more.)
    # Получи ее номинал с помощью:  coin.value
    totalGold += coin.value

    if totalGold >= 25:
        # >= означает, что "totalGold" превысил значение 25.
        # Это прерывает цикл, чтобы запустить код внизу.
        break  # Завершил сбор золота!
hero.moveXY(58, 33)
# Подойди к Нарии и сообщи, сколько золота ты собрал.
hero.say(hero.gold)
