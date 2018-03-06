class Game:
    summonTypes = ['paladin']
    excludeType = ['door', 'decoy']
    priorityType = []
    tacticks = {        'skeleton': 'attack',        'paladin': 'defend'    }

    def __init__(self):
        self.team = hero.team
        self.best_target = None
        self.best_target_distance = 9999
        hero._earthskin = -10

    def findTarget(self):  # exclude  decoy
        best = 0
        enemies = hero.findEnemies()
        self.best_target = None
        self.best_target_distance = 9999
        self.enemy_hero = [e for e in hero.findEnemies() if e.id in ["Hero Placeholder", "Hero Placeholder 1"]][0]
        for enemy in enemies:
            if enemy.type in self.excludeType:
                continue
            distance = hero.distanceTo(enemy)
            current = enemy.maxHealth / distance
            # hero.debug(enemy.id,enemy.type, current)
            if (best > current):
                best = current
                self.best_target = enemy
                self.best_target_distance = distance

        if (not (self.best_target)):
            self.best_target = hero.findNearestEnemy()
            self.best_target_distance = hero.distanceTo(self.best_target)

        if (self.enemy_hero and hero.distanceTo(self.enemy_hero) < 90):
            self.best_target = self.enemy_hero
            self.best_target_distance = hero.distanceTo(self.best_target)

        hero.debug("best target", self.best_target)

    def moveTo(self, position):
        if (hero.isReady("jump")):
            hero.jumpTo(position)
        else:
            hero.move(position)

    def summonTroops(self):
        type = self.summonTypes[len(hero.built) % len(self.summonTypes)]
        if hero.gold > hero.costOf(type):
            hero.summon(type)

    def commandTroops(self):
        for friend in hero.findFriends():
            if friend.type == 'paladin':
                self._commandPaladin(friend)
            elif friend.type == 'soldier' or friend.type == 'archer' or friend.type == 'griffin-rider' or friend.type == 'skeleton':
                self._commandSoldier(friend)
            elif friend.type == 'peasant':
                self._commandPeasant(friend)

    def _commandSoldier(self, soldier):
        if self.best_target and soldier.distanceTo(self.best_target) < 30:
            hero.command(soldier, "attack", self.best_target)
        else:
            hero.command(soldier, "defend", hero)

    def _commandPeasant(self, soldier):
        item = soldier.findNearestItem()
        if item:
            hero.command(soldier, "move", item.pos)

    def _commandPaladin(self, paladin):
        if (paladin.canCast("heal") and hero.health < hero.maxHealth * 2 / 3):
            hero.command(paladin, "cast", "heal", hero)
        else:
            if self.best_target and paladin.distanceTo(self.best_target) < 30:
                hero.command(paladin, "attack", self.best_target)
            else:
                hero.command(paladin, "defend", hero)

    def pickUpNearestItem(self, items):
        nearestItem = hero.findNearest(items)
        if nearestItem:
            moveTo(nearestItem.pos)

    def attack(self):
        # todo: mass targets
        if self.best_target is not None:
            if (hero.canCast('fear', self.best_target) and self.best_target_distance < 25):
                hero.cast('fear', self.best_target)
            elif (hero.canCast('drain-life', self.best_target) and self.best_target_distance < 15):
                hero.cast('drain-life', self.best_target)
            elif (hero.canCast('poison-cloud',
                               self.best_target) and self.best_target_distance < 30 and self.best_target_distance > 10):
                hero.cast('poison-cloud', self.best_target)
            elif (hero.canCast('chain-lightning', self.best_target) and self.best_target_distance < 30):
                hero.cast('chain-lightning', self.best_target)
            else:
                hero.attack(self.best_target)

    def _canDevour(self):
        if not (hero.isReady('devour')):
            return None
        enemy = hero.findNearestEnemy()  # todo: not only closest
        if (enemy and enemy.health < 200):
            return enemy
        return None

    def _action(self):
        devourTarget = self._canDevour()
        # if(hero.health<hero.maxHealth/3):
        # hero.devour(enemy)
        if (devourTarget):
            hero.devour(devourTarget)
            return
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
            return
        if (hero.canCast('earthskin', hero) and hero.now() > 3):
            hero.cast('earthskin', hero)
            self._earthskin = hero.now()
            return
        if (hero.canCast('raise-dead')):
            courpses = hero.findCorpses()
            closest = 0
            for courpse in courpses:
                if (hero.distanceTo(courpse) <= 20):
                    closest += 1
                if (closest > 5):
                    hero.cast('raise-dead')
                    return
        if (hero.canCast('summon-undead')):  # todo: check for bodies
            hero.cast('summon-undead')
            return
        self.attack()

    def run(self):
        self.findTarget()
        self.summonTroops()
        self.commandTroops()
        self._action()


def onSpawn(e):
    while True:
        enemy = hero.findNearestEnemy()  # todo: list of closest
        if enemy and pet.isReady("chase") and enemy.maxHealth < enemy.maxHealth / 1:
            pet.chase(enemy)
        # Find and fetch a "potion":
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)


pet.on('spawn', onSpawn)
game = Game()
while True:
    game.run()
