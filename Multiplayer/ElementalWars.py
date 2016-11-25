# http://codecombat.com/play/level/elemental-wars
# Победите героя противника менее, чем за три минуты.

def buildArmy():
    # Ваш герой может вызывать дружественные отряды и управлять ими.

    buildOrder = ["water-soldier", "wood-soldier", "fire-soldier", "wood-soldier", "wood-soldier", "archer", "soldier",
                  "water-soldier", "wood-soldier", "fire-soldier", "wood-soldier", "wood-soldier", "archer", "soldier",
                  "water-soldier", "wood-soldier", "fire-soldier", "wood-soldier", "wood-soldier", "archer", "soldier",
                  "water-soldier", "wood-soldier", "fire-soldier", "wood-soldier", "wood-soldier", "archer", "soldier",
                  "wood-artillery"]
    # "arrow-tower" "artillery"
    type = buildOrder[len(hero.built) % len(buildOrder)]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)


def commandArmy():
    friends = hero.built
    enemies = hero.findEnemies()
    points = hero.getControlPoints()
    for i, friend in enumerate(friends):
        if friend.health <= 0 or friend.type == "arrow-tower":
            continue
        # Управляйте своей армией, чтобы захватить ключевые точки.
        # Убедитесь, что ключевые точки выбраны с умом!

        point = points[i % len(points)]
        if hero.now() < 30:
            hero.command(friend, "defend", point.pos)
        else:
            enemies = hero.findEnemies()
            nearestEnemy = hero.findNearest(enemies)
            hero.command(friend, "attack", nearestEnemy)


def attack(target):
    if target:
        if hero.isReady("throw") and hero.distanceTo(target) < hero.throwRange:
            hero.throw(target)
        elif (hero.distanceTo(target) > 10):
            hero.move(target.pos)
        elif (hero.isReady("stomp") and hero.distanceTo(target) < 5):
            hero.stomp()
        elif (hero.isReady("attack")):
            hero.attack(target)


def controlHero():
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)
    shouldAttack = hero.now() > 30
    # Используйте возможности героя, чтобы переломить ситуацию в свою пользу.
    if shouldAttack:
        attack(nearestEnemy)


while True:
    buildArmy()
    commandArmy()
    controlHero()
