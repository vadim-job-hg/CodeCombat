# Hushbaum попал в засаду огров!
# Она занята исцелением своих солдат. Вам следуют отдать им приказ сражаться!
# Огры могут вызвать подкрепление, если посчитают, что смогут добраться до Hushbaum'а или ваших лучников. Поэтому держите их в оборонительном кольце!
def summonSoldier():
    # Заполни код здесь, что призвать солдата, если у тебя достаточно золота.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")


# Солдаты формируют круг и защищаются.
def commandSoldier(soldier, soldierIndex, numSoldiers):
    angle = Math.PI * 2 * soldierIndex / numSoldiers
    defendPos = {"x": 41, "y": 40}
    defendPos.x += 10 * Math.cos(angle)
    defendPos.y += 10 * Math.sin(angle)
    if (soldier.health > 60):
        hero.command(soldier, "defend", defendPos)
    else:
        hero.command(soldier, "defend", {'x': 42, 'y': 40})


# Найдите самую крепкую цель (больше всего здоровья)
# Эта функция что-то возвращает! Когда Вы вызываете функцию, то получаете от неё какое-то значение.
def findStrongestTarget():
    mostHealth = 0
    bestTarget = None
    enemies = hero.findEnemies()
    # Определите, у какого из врагов больше всего уровень здоровья и направьте метод bestTarget на этого врага.

    # Концентрируйте огонь лучников на одного противника только в том случае, когда нападает большой огр.
    if bestTarget and bestTarget.health > 15:
        return bestTarget
    else:
        return None


# Если у врага, определенного как strongestTarget больше 15 единиц здоровья, атакуйте его. Иначе, атакуйте ближайшего врага.
def commandArcher(archer):
    nearest = archer.findNearestEnemy()
    if archerTarget:
        hero.command(archer, "attack", archerTarget)
    elif nearest:
        hero.command(archer, "attack", nearest)


archerTarget = None

while True:  # Если враг, определенный как archerTarget мертв или не существует, найдите нового.
    if not archerTarget or archerTarget.health <= 0:
        # Установите целью (или "аргументом") функции archerTarget, значение, возвращенное функцией findStrongestTarget().
        archerTarget = findStrongestTarget()

    friends = hero.findFriends()
    soldiers = hero.findByType("soldier")
    archers = hero.findByType("archer")
    for i, soldier in enumerate(soldiers):
        commandSoldier(soldier, i, len(soldiers));
    summonSoldier()
    # Используйте функцию commandArcher() для управления своими лучниками.
    for i, archer in enumerate(archers):
        commandArcher(archer);
