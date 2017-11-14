# Ogrovia ťa chytajú do pasce svojimi temnými  rituálmi!
# Tvoj hrdina nemôže robiť nič iné okrem command a move bez toho abz si rozčúlil čarodejníkov.
# Pozor na ľad, robotov, pasce, antigravitačné polia, a ostatnú čiernu mágiu.
# Nejako, musíš poraziť Nalfara a zachrániť svojho paladina.
# Veľé poklady Kelvintapha očakávajú tvoje víťazstvo.
step = 0


def choiseTarget(enemies):
    hero.say(enemies)
    for enemy in enemies:
        for att in attack:
            if att[0] == enemy.pos.x and att[1] == enemy.pos.y:
                return enemy
    return None


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if (step == 0 and friend.pos.y > 60 and (friend.type != 'archer' or hero.now() > 3.6)):
            enemy = friend.findNearestEnemy()
            if enemy:
                hero.command(friend, "attack", enemy)
        elif step == 4:
            hero.command(friend, "move", {'x': 42, 'y': 67})
        elif friend.type == 'archer':
            CommandArcher(friend)
        elif friend.type == 'paladin':
            CommandPaladin(friend)
        else:
            CommandSoldier(friend)


def CommandPaladin(soldier):
    if step < 4:
        if (soldier.canCast("heal") and hero.now() > 3.0):
            hero.command(soldier, "cast", "heal", soldier)
        elif hero.now() > 2.8 and soldier.health < soldier.maxHealth * 0.7:
            hero.command(soldier, "shield")


def CommandSoldier(soldier):
    if step < 4:
        if soldier.pos.x < 74:
            hero.command(soldier, "move", {'x': 76, 'y': 76})
        else:
            enemy = soldier.findNearestEnemy()
            if enemy:
                hero.command(soldier, "attack", enemy)


def CommandArcher(soldier):
    if step == 1:
        if soldier.pos.y > 60:
            hero.command(soldier, "move", {'x': 22, 'y': 55})
        else:
            enemies = soldier.findEnemies()
            for enemy in enemies:
                if enemy.type != 'yeti':
                    hero.command(soldier, "attack", enemy)
    elif step == 2:
        if soldier.pos.x > 14:
            hero.command(soldier, "move", {'x': 8, 'y': 77})
        else:
            enemy = soldier.findNearestEnemy()
            if enemy:
                hero.command(soldier, "attack", enemy)
    elif step == 3:
        if soldier.pos.x < 74:
            hero.command(soldier, "move", {'x': 76, 'y': 76})
        else:
            enemy = soldier.findNearestEnemy()
            if enemy:
                hero.command(soldier, "attack", enemy)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


index = 0
route = [[33, 12, False], [34, 9, False], [32, 6, False]]


def moveHero():
    if len(route) > index:
        moveTo({'x': route[index][0], 'y': route[index][1]}, route[index][2])
        if (hero.pos.x == route[index][0] and hero.pos.y == route[index][1]):
            return True
        else:
            return False


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        else:
            hero.attack(target)


while True:
    if (hero.now() > 6 and hero.now() < 12):
        step = 1
    elif (hero.now() > 10 and hero.now() < 17):
        step = 2
    elif (hero.now() > 15 and hero.now() < 29):
        step = 3
    elif (hero.now() > 27 and hero.now() < 600):
        step = 4
    commandTroops()
    if step < 4:
        if moveHero():
            index = index + 1
    else:
        enemy = hero.findNearest(hero.findEnemies())
        if enemy:
            attack(enemy)
        else:
            moveTo({'x': 74, 'y': 44})
