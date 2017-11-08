# http://codecombat.com/play/level/gas-attack
# Крестьяне находятся в ловушке в долине!
# У вас есть только одна защиту от яда.
# Calculate the require mass of the shell to defeat the ogres.
# The poison mass needs to be equal to the health of the ogres.
# Использование слишком малого или слишком большого приведет к аварии!

# Эта функция возвращает общее число здоровья врагов.
def healthSum(units):
    # Создайте переменный набор от 0, чтобы начать сумму.
    summ = 0
    for unit in units:
        summ = summ + unit.health
    # Итератор через каждого врага в массиве и добавьте их здоровье к переменной суммы.

    return summ  # ∆ Измените это, чтобы возвратить суммарную переменную!


# Используйте орудие чтобы победить огров.
cannon = hero.findNearest(hero.findFriends())

# Орудие можно видеть через стены.
enemies = cannon.findEnemies()

# Посчитайте сумму здоровья Манчкинов.
hero.say("Используй " + healthSum(enemies) + " граммы.")
