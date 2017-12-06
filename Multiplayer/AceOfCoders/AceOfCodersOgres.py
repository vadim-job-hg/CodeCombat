def buildArmy():
    buildOrder = ["soldier", "soldier", "soldier", "soldier", "soldier", "soldier", "soldier", "soldier", "soldier",
                  "soldier", "archer", "soldier", "archer", "soldier", "archer"]
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
    if shouldAttack:
        attack(nearestEnemy)


while True:
    buildArmy()
    commandArmy()
    controlHero()