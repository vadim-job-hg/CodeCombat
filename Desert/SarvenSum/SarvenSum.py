# https://codecombat.com/play/level/sarven-sum
# Чтобы отключить огненные ловушки, добавьте значение lowest.trap к максимальному значению.
# Идите к белому кресту и скажите Китти ответ.
# Сокрушите всех огров, если осмелитесь
# Как только все огры повершены, идите к красному кресту.
# Остерегайтесь яда, чтобы сохранить здоровье.
def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider' or friend.type == 'skeleton':
            CommandSoldier(friend)


def CommandSoldier(soldier):
    hero.command(soldier, "defend", hero)

def moveTo(position, fast=True):
    if position:
        if (hero.isReady("jump") and fast):
            hero.jumpTo(position)
        else:
            hero.move(position)


summonTypes = ['soldier','soldier','soldier','soldier','soldier','soldier']


def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold > hero.costOf(type):
        hero.summon(type)
        commandTroops()


def attack(target):
    if target:
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('summon-undead')):
            hero.cast('summon-undead')
        elif (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        elif (hero.canCast('drain-life', target)):
            hero.cast('drain-life', target)
        else:
            if (hero.canCast('earthskin', self)):
                hero.cast('earthskin', self)
            elif (hero.canCast('chain-lightning', target)):
                hero.cast('chain-lightning', target)
            else:
                hero.attack(target)

whiteX = {'x':27, 'y':42}
redX = {'x':151 , 'y': 118}
hero.moveXY(whiteX.x, whiteX.y)
hazards = hero.findHazards()
max = 0
min = 999
for hazard in hazards:
    if hazard.value> max:
        max = hazard.value
    if hazard.value< min:
        min = hazard.value
hero.say(max + min)
while True:
    summonTroops()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        attack(enemy)
    elif item:
        hero.move(item.pos)
    else:
        hero.move(redX)
