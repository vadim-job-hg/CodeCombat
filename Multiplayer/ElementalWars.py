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
    type = buildOrder[len(self.built) % len(buildOrder)]
    if self.gold >= self.costOf(type):
        self.summon(type)


def commandArmy():
    friends = self.built
    enemies = self.findEnemies()
    points = self.getControlPoints()
    for i, friend in enumerate(friends):
        if friend.health <= 0 or friend.type == "arrow-tower":
            continue
        # Управляйте своей армией, чтобы захватить ключевые точки.
        # Убедитесь, что ключевые точки выбраны с умом!

        point = points[i % len(points)]
        if self.now() < 30:
            self.command(friend, "defend", point.pos)
        else:
            enemies = self.findEnemies()
            nearestEnemy = self.findNearest(enemies)
            self.command(friend, "attack", nearestEnemy)


def attack(target):
    if target:
        if self.isReady("throw") and self.distanceTo(target) < self.throwRange:
            self.throw(target)
        elif (self.distanceTo(target) > 10):
            self.move(target.pos)
        elif (self.isReady("stomp") and self.distanceTo(target) < 5):
            self.stomp()
        elif (self.isReady("attack")):
            self.attack(target)


def controlHero():
    enemies = self.findEnemies()
    nearestEnemy = self.findNearest(enemies)
    shouldAttack = self.now() > 30
    # Используйте возможности героя, чтобы переломить ситуацию в свою пользу.
    if shouldAttack:
        attack(nearestEnemy)


loop:
buildArmy()
commandArmy()
controlHero()
