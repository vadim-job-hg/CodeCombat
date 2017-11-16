enemy_types = {}
# ogres types
enemy_types['door'] = {'danger': 1000, 'focus': 200}
enemy_types['knight'] = {'danger': 100, 'focus': 100}
enemy_types['potion-master'] = {'danger': 100, 'focus': 100}
enemy_types['ranger'] = {'danger': 100, 'focus': 100}
enemy_types['trapper'] = {'danger': 100, 'focus': 100}
enemy_types['samurai'] = {'danger': 100, 'focus': 100}
enemy_types['librarian'] = {'danger': 100, 'focus': 100}
enemy_types['sorcerer'] = {'danger': 100, 'focus': 100}
enemy_types['hero-placeholder'] = {'danger': 99, 'focus': 100}
enemy_types['hero-placeholder-1'] = {'danger': 99, 'focus': 100}
enemy_types['hero-placeholder-2'] = {'danger': 99, 'focus': 100}
enemy_types['necromancer'] = {'danger': 100, 'focus': 100}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['goliath'] = {'danger': 100, 'focus': 50}
enemy_types['captain'] = {'danger': 100, 'focus': 100}
enemy_types['forest-archer'] = {'danger': 100, 'focus': 50}
enemy_types['ninja'] = {'danger': 100, 'focus': 50}
enemy_types['skeleton'] = {'danger': 5, 'focus': 22}
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
if hero.team == 'humans':
    team = 'humans'
else:
    team = 'ogres'

def findTarget():
    danger = 0
    enemy_return = None
    for type in enemy_types.keys():
        if enemy_types[type] and enemy_types[type].danger > danger:
            enemy = hero.findNearest(hero.findByType(type))
            if enemy and enemy.team != team and hero.distanceTo(enemy) < enemy_types[type].focus and enemy.type!='door' and enemy.pos.x>80:
                enemy_return = enemy
                danger = enemy_types[type].danger
    if enemy_return is None:
        enemy_return = hero.findNearest(hero.findEnemies())
    if enemy_return and enemy_return.type=='door':
        enemy_return = None
    return enemy_return

def moveTo(position):
    if position:
        if (hero.isReady("jump")):
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
        elif friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider'  or friend.type == 'skeleton':
            CommandSoldier(friend)
        elif friend.type == 'peasant':
            CommandPeasant(friend)

def CommandSoldier(soldier):
    hero.command(soldier, "defend", hero)

def CommandPeasant(soldier):
    item = soldier.findNearestItem()
    if item:
        hero.command(soldier, "move", item.pos)

def CommandPaladin(paladin):
    if (paladin.canCast("heal") and hero.health<hero.maxHealth):
        hero.command(paladin, "cast", "heal", self)
    else:
        hero.command(paladin, "shield")

def pickUpNearestItem(items):
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)

def attack():
    target = findTarget()
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (hero.canCast('fear', target) and hero.distanceTo(target)<25):
            hero.cast('fear', target)
        elif (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        elif (hero.canCast('drain-life', target) and hero.distanceTo(target)<15):
            hero.cast('drain-life', target)
        elif (hero.canCast('poison-cloud', target) and hero.distanceTo(target)<30):
            hero.cast('poison-cloud', target)
        else:
            if (hero.canCast('chain-lightning', target) and hero.distanceTo(target)<30):
                hero.cast('chain-lightning', target)
            else:
                hero.attack(target)

while True:
    commandTroops()
    if (hero.canCast('earthskin', self)):
        hero.cast('earthskin', self)
    attack()
    summonTroops()
