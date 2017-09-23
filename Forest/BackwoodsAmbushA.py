# https://codecombat.com/play/level/backwoods-ambush-a
# На этом уровне ты будешь использовать функции с двумя параметрами
# Посмотри на код ниже, обрати внимание на использование двух аргументов.
# Оба доступны внутри функции.

def checkAndAttack(x, y):
    # Сначала двигайся к координатам, заданным параметрами.
    hero.moveXY(x, y)
    # Затем проверь наличие врага.
    enemy = hero.findNearestEnemy()
    if enemy:
        # Увидел врага - атакуй его!
        while enemy.health>0:
            hero.attack(enemy)
    pass

checkAndAttack(24, 42)
checkAndAttack(27, 60)
# Направляйся к последним трём отметкам X и убей оставшихся манчкинов.
checkAndAttack(43, 51)
checkAndAttack(39, 25)
checkAndAttack(55, 29)
