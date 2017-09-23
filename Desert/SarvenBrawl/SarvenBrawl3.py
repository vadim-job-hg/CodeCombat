enemy_types = {}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 10}
enemy_types['warlock'] = {'danger': 10, 'focus': 10}
# enemy_types['burl'] = {'danger':10, 'focus':5}
enemy_types['witch'] = {'danger': 8, 'focus': 10}
# enemy_types['brawler'] = {'danger':7, 'focus':5}
# enemy_types['ogre'] = {'danger':5, 'focus':5}
# enemy_types['chieftain'] = {'danger':6, 'focus':10}
enemy_types['fangrider'] = {'danger': 4, 'focus': 20}
# enemy_types['skeleton'] = {'danger':5, 'focus':10}
# enemy_types['scout'] = {'danger':4, 'focus':10}
# enemy_types['thrower'] = {'danger':3, 'focus':15}
# enemy_types['munchkin'] = {'danger':2, 'focus':5}
enemy_types['yak'] = {'danger': -1, 'focus': 0}
enemy_types['ice-yak'] = {'danger': -1, 'focus': 0}

if hero.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'


def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and enemy.type != 'yak' and enemy.team != team and hero.distanceTo(enemy) < enemy_types[
                type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    # if enemy_return is None:
    #    enemy_return =  hero.findNearestEnemy()
    if enemy_return and enemy_return.type != 'yak':
        return enemy_return
    else:
        return None


def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


summonTypes = ['paladin']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)


def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier' or friend.type == 'archer':
            CommandSoldier(friend)


def CommandSoldier(soldier):
    target = hero.findNearestEnemy()
    if target:
        hero.command(soldier, "attack", target)


def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health < hero.maxHealth * 0.9):
        hero.command(paladin, "cast", "heal", self)
    else:
        if enemyattack:
            hero.command(paladin, "attack", enemyattack)
        else:
            hero.command(paladin, "defend", self)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target) and yak_alert == False):
            hero.cast('chain-lightning', target)
        elif (hero.isReady("attack")):
            hero.attack(target)
        else:
            hero.shield()


index = 0
route = [[20, 20, True], [140, 20, True], [140, 117, True], [20, 110, True]]


def moveHero():
    ind = index % len(route)
    moveTo({'x': route[ind][0], 'y': route[ind][1]}, route[ind][2])
    if (hero.pos.x == route[ind][0] and hero.pos.y == route[ind][1]):
        return True
    else:
        return False


while True:
    yak_alert = False
    enemyattack = findTarget()
    yak = hero.findNearest(hero.findByType('sand-yak'))
    if yak and hero.distanceTo(yak) < 40:
        yak_alert = True
    commandTroops()
    summonTroops()
    if enemyattack:
        attack(enemyattack)
    elif (moveHero()):
        index = index + 1
