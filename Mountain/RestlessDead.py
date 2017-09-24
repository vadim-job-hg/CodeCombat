# https://codecombat.com/play/level/restless-dead
# Этот уровень считается ОЧЕНЬ сложным! Чтобы одолеть его, тебе понадобится хорошая стратегия или эпичное барахлишко!

# Найди и убей йети, чтобы добыть его кровь для ритуала.
# Возможно, тебе стоит собрать монеты, которые оставит йети. Они пригодятся, чтобы вызвать подкрепление.
# Встань на ритуальный камень (красная отметка Х) для призвания.
# Теперь всё просто: нужно пережить нашествие орд нежити.
summonTypes = ['paladin']


def attack(enemy):
    if enemy:
        while (enemy.health > 0):
            if (hero.distanceTo(enemy) > 10):
                hero.move(enemy.pos)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            elif (hero.canCast('chain-lightning', enemy)):
                hero.cast('chain-lightning', enemy)
            else:
                hero.attack(enemy)


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)


def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health < hero.maxHealth * 0.6):
        hero.command(paladin, "cast", "heal", hero)
    else:
        hero.command(paladin, "defend", hero)


def collectItems():
    item = hero.findNearestItem()
    while item:
        hero.move(item.pos)
        item = hero.findNearestItem()


hero.moveXY(55, 10)
hero.wait(2)
attack(hero.findNearestEnemy())
collectItems()
hero.moveXY(55, 33)
hero.moveXY(49, 37)
hero.moveXY(19, 40)
for i in range(1, 20):
    summonTroops()
commandTroops()
hero.moveXY(55, 48)
while True:
    attack(hero.findNearestEnemy())
    commandTroops()
    collectItems()
