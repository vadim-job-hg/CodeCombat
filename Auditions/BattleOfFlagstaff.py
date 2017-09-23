# http://codecombat.com/play/level/battle-of-flagstaff
enemy_types = {}
# humans hero types
enemy_types['knight'] = {'danger': 100, 'focus': 100}
enemy_types['ranger'] = {'danger': 100, 'focus': 100}
enemy_types['librarian'] = {'danger': 100, 'focus': 100}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['trapper'] = {'danger': 100, 'focus': 100}
enemy_types['samurai'] = {'danger': 100, 'focus': 50}
enemy_types['forest-archer'] = {'danger': 100, 'focus': 50}
enemy_types['sorcerer'] = {'danger': 100, 'focus': 50}
# ogres types
enemy_types['shaman'] = {'danger': 10, 'focus': 100}
enemy_types['warlock'] = {'danger': 10, 'focus': 30}
enemy_types['arrow-tower'] = {'danger': 10, 'focus': 20}
enemy_types['catapult'] = {'danger': 10, 'focus': 100}
enemy_types['burl'] = {'danger': 10, 'focus': 20}
enemy_types['artillery'] = {'danger': 10, 'focus': 100}
enemy_types['witch'] = {'danger': 8, 'focus': 100}
enemy_types['brawler'] = {'danger': 7, 'focus': 55}
enemy_types['ogre'] = {'danger': 5, 'focus': 40}
enemy_types['chieftain'] = {'danger': 6, 'focus': 35}
enemy_types['fangrider'] = {'danger': 4, 'focus': 22}
enemy_types['skeleton'] = {'danger': 5, 'focus': 22}
enemy_types['scout'] = {'danger': 4, 'focus': 22}
enemy_types['thrower'] = {'danger': 3, 'focus': 22}
enemy_types['munchkin'] = {'danger': 2, 'focus': 15}
enemy_types['yak'] = {'danger': -1, 'focus': 0}
enemy_types['ice-yak'] = {'danger': -1, 'focus': 0}


def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


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
            if enemy and enemy.team != team and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if enemy_return is None:
        enemy_return = hero.findNearestEnemy()
    return enemy_return


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
    if (paladin.canCast("heal")):
        if (hero.health < hero.maxHealth * 0.6):
            target = self
        if target:
            hero.command(paladin, "cast", "heal", target)
    else:
        target = hero.findNearestEnemy()
        hero.command(paladin, "attack", target)


def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)


while True:
    flag = hero.findFlag()
    summonTroops()
    commandTroops()
    if flag:
        hero.pickUpFlag(flag)
    else:
        enemy = findTarget()
        if enemy:
            attack(enemy)
        else:
            items = hero.findItems()
            pickUpNearestItem(items)
            # find some enemy to attack
            # use cleave when ready
