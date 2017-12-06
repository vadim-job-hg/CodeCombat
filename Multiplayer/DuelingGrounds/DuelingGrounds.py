enemy_types = {}
# enemy_types['door'] = {'danger':1000, 'focus':200}
enemy_types['knight'] = {'danger': 100, 'focus': 50}
enemy_types['ranger'] = {'danger': 100, 'focus': 50}
enemy_types['trapper'] = {'danger': 100, 'focus': 50}
enemy_types['samurai'] = {'danger': 100, 'focus': 50}
enemy_types['sorcerer'] = {'danger': 100, 'focus': 50}
enemy_types['burl'] = {'danger': 10, 'focus': 20}
enemy_types['necromancer'] = {'danger': 100, 'focus': 50}
enemy_types['captain'] = {'danger': 100, 'focus': 50}
enemy_types['shaman'] = {'danger': 10, 'focus': 50}
enemy_types['warlock'] = {'danger': 10, 'focus': 30}
enemy_types['arrow-tower'] = {'danger': 10, 'focus': 20}
enemy_types['catapult'] = {'danger': 10, 'focus': 100}
enemy_types['artillery'] = {'danger': 10, 'focus': 100}
enemy_types['witch'] = {'danger': 8, 'focus': 50}
enemy_types['brawler'] = {'danger': 7, 'focus': 55}
enemy_types['ogre'] = {'danger': 5, 'focus': 40}
enemy_types['chieftain'] = {'danger': 6, 'focus': 35}
enemy_types['thrower'] = {'danger': 3, 'focus': 22}
enemy_types['fangrider'] = {'danger': 4, 'focus': 22}
enemy_types['munchkin'] = {'danger': 2, 'focus': 15}
enemy_types['yak'] = {'danger': -1, 'focus': 0}
enemy_types['ice-yak'] = {'danger': -1, 'focus': 0}

def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and hero.distanceTo(enemy) < enemy_types[type].focus:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if not(enemy_return):
        enemy_return = hero.findNearest(hero.findEnemies())
    return enemy_return

def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)

def moveTo(position, fast=True):
    if (hero.isReady("jump") and hero.distanceTo(position) > 10 and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)

def attack(target):
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        #elif (hero.canCast('raise-dead')):
        #    hero.cast('raise-dead')
        elif (hero.canCast('drain-life', target) and hero.distanceTo(target)<30):
            hero.cast('drain-life', target)
        elif (hero.canCast('poison-cloud', target) and hero.distanceTo(target)<30):
            hero.cast('poison-cloud', target)
        elif (hero.canCast('fear', target)):
            hero.cast('fear', target)
        elif (hero.canCast('earthskin', hero)):
            hero.cast('earthskin', hero)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)

summonTypes = ['paladin']
def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)

def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)
        elif friend.type == 'paladin':
            CommandPaladin(friend)
        elif friend.type == 'soldier' or friend.type == 'skeleton':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)

def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health < hero.maxHealth * 0.6):
        hero.command(paladin, "cast", "heal", hero)
    elif (paladin.health < 10):
        hero.command(paladin, "shield")
    else:
        hero.command(paladin, "defend", hero)

def CommandSoldier(soldier):
    hero.command(soldier, "defend", hero)

def CommandArcher(soldier):
    hero.command(soldier, "defend", hero)

def CommandPeasant(soldier):
    pass

def lowestHealthFriend():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend
    return lowestFriend

while True:
    summonTroops()
    commandTroops()
    items = hero.findItems()
    enimies = hero.findEnemies()
    if (len(items) > 0 and hero.health < hero.maxHealth * 0.5):
        pickUpNearestItem(items)
    else:
        enemyattack = findTarget()
        if (enemyattack):
            attack(enemyattack)
        else:
            hero.wait(1)
