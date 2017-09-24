# https://codecombat.com/play/level/sowing-fire
# Цель: построй три ряда из 9 ловушек.

# Возвращает "retreat", "attack", "start-next-trap-column" или "build-next-trap-in-column"
def chooseStrategy():
    enemies = hero.findEnemies()

    # В случае превосходящих сил противника верни "retreat" (отступление).
    if len(enemies) > 20:
        return "retreat"
    # Если есть несколько огров, верни "attack" (атаковать).
    if len(enemies) > 0:
        return "attack"
    # Сравни `x % 9` с 0, чтобы проверить делимость x на 9.
    # Используй `len(self.built)` для определения количества построенных ловушек.
    # Если ты закончил колонку из 9 ловушек, верни "start-next-trap-column" (начать новую колонку).
    if len(self.built) % 9 == 0:
        return "start-next-trap-column"
    # Иначе верни "build-next-trap-in-column" (построить следующую ловушку в ряду).
    else:
        return "build-next-trap-in-column"


trapsInColumn = 9
startX = 40
columnX = startX


# Построй следующую ловушку в ряду на правильном месте.
def buildNextTrapInColumn(columnX, numTraps):
    # Измени `newY` на использование `%`, чтобы зациклиться и строить `trapsInColumn` (9) ловушек в ряду.
    newY = 7 * (numTraps % 9) + 10  # ∆ Измени это, используя `% 9`!
    if hero.pos.y < newY:
        hero.move({"x": columnX - 5, "y": newY})
    else:
        buildTrap(columnX, newY)


# Начни новую колонку ловушек.
def startNextTrapColumn(columnX, numTraps):
    newX = startX - (Math.floor(numTraps / trapsInColumn) * 6)
    if hero.pos.y > 10:
        hero.move({"x": newX - 5, "y": 10})
        return columnX
    else:
        buildTrap(newX, 10)
        return newX


def buildTrap(x, y):
    hero.buildXY("fire-trap", x, y)


def commandAttack():
    # Пусть твои всадники на гриффинах отгонят атакующих.
    for friend in hero.findFriends():
        enemy = friend.findNearestEnemy()
        if enemy:
            hero.command(friend, 'attack', enemy)
    pass


def commandRetreat():
    hero.say("Retreat!")
    # Ты вместе со всадниками отступаешь в безопасную область за ловушками.
    hero.moveXY(4, 42)
    for friend in hero.findFriends():
        hero.command(friend, 'move', Vector(24, friend.pos.y))


while True:
    strategy = chooseStrategy()
    if strategy == "attack":
        commandAttack()
    elif strategy == "build-next-trap-in-column":
        buildNextTrapInColumn(columnX, len(hero.built))
    elif strategy == "start-next-trap-column":
        columnX = startNextTrapColumn(columnX, len(hero.built))
    elif strategy == "retreat":
        commandRetreat()
