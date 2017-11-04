excepE = ['tower']
dest = {'x': 78, 'y': 39}
done = False


def getPos(obj):
    return obj.pos.x, obj.pos.y


def toPos(x, y):
    return {'x': x, 'y': y}


def rushTo(xy):
    if hero.isReady("jump"):
        hero.jumpTo(xy)
    hero.move(xy)


def exclude(units, exceps):
    return [u for u in units if u.type not in exceps]


def farthest(enemies):
    farthestD = 0
    for enemy in enemies:
        d = hero.distanceTo(enemy)
        if d > farthestD and enemy.health > 0:
            farthestD = d
            farthest = enemy
    return farthest


def nearby(enemies, dis):
    return sum([hero.distanceTo(e) < dis for e in enemies])


def selfDying(self):
    if self.health < self.maxHealth / 2:
        hero.command(self, "move", {'x': self.pos.x - 1, 'y': self.pos.y})


def evade():
    x, y = getPos(hero)
    orbs = hero.findEnemyMissiles()
    if len(orbs):
        orb = hero.findNearest(orbs)
        if hero.distanceTo(orb) < 3:
            if y > 14:
                hero.moveXY(x, y - 7)
            else:
                hero.moveXY(x, y + 7)


def lowHP():
    friends = hero.findFriends()
    lowest = 9999
    dying = None
    if len(friends):
        for friend in friends:
            hp = friend.health
            if hp < friend.maxHealth / 3 and hp < lowest and hp > 0:
                lowest = hp
                dying = friend
    return dying


def soldierAtk(soldier):
    selfDying(soldier)
    enemies = hero.findByType("ogre")
    if not len(enemies):
        enemy = soldier.findNearestEnemy()
    else:
        enemy = enemies[0]
    if enemy:
        hero.command(soldier, "attack", enemy)
    else:
        hero.command(soldier, "move", soldier.pos)


def archerAtk(archer):
    enemies = hero.findByType("chieftain")
    if not len(enemies):
        enemy = archer.findNearestEnemy()
    else:
        enemy = enemies[0]
    if enemy and archer.pos.x > 53 and archer.pos.y < 40:
        hero.command(archer, "attack", enemy)
    elif hero.time > 6:
        hero.command(archer, "move", dest)


def riderAtk(rider):
    enemies = hero.findByType("robot-walker")
    if len(enemies):
        hero.command(rider, "move", {'x': enemies[0].pos.x / 2 + enemies[1].pos.x / 2,
                                     'y': enemies[0].pos.y / 2 + enemies[1].pos.y / 2})


def palaAtk(pala):
    selfDying(pala)
    dying = lowHP()
    enemies = hero.findByType("witch")
    if not len(enemies):
        enemy = pala.findNearestEnemy()
    else:
        enemy = enemies[0]
    if dying and pala.canCast('heal'):
        hero.command(pala, "cast", 'heal', dying)
    else:
        hero.command(pala, "move", dest)
    if pala.canCast('heal') and hero.health < 2 * hero.maxHealth / 3:
        hero.command(pala, "cast", 'heal', hero)
    if pala.pos == dest:
        hero.command(pala, "shield")


def summon(soldier):
    while hero.gold >= hero.costOf(soldier):
        hero.summon(soldier)


def command():
    for unit in hero.findFriends():
        t = unit.type
        if t == 'griffin-rider':
            riderAtk(unit)
        elif t == 'soldier':
            soldierAtk(unit)
        elif t == 'paladin':
            palaAtk(unit)
        elif t == 'archer':
            archerAtk(unit)


def atk():
    if hero.gold > hero.costOf('griffin-rider'):
        hero.summon('griffin-rider')
    command()

    enemies = hero.findByType("robot-walker")
    if len(enemies):
        pass
    else:
        enemy = hero.findNearest([e for e in hero.findEnemies() if e.type not in ['ice-yak', 'cow']])
        if enemy:
            command()
            if hero.canCast("chain-lightning", enemy) and hero.time > 7:
                hero.cast("chain-lightning", enemy)
        elif not len(enemies):
            hero.move({'x': 78, 'y': 14})
    return True


def run():
    while True:
        evade()
        atk()


run()
