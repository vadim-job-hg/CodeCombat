class Game:
    summonTypes = ['paladin']
    excludeType = ['decoy']
    priorityType = []
    tacticks = {'skeleton': 'attack', 'paladin': 'defend'}

    def __init__(self):
        self.team = hero.team
        if self.team == 'humans':
            self.position = 'left'
        else:
            self.position = 'right'
        hero.debug("self.position", self.position)
        self.best_target = None
        self.best_target_distance = 9999
        hero._earthskin = -10

    def findTarget(self):  # exclude  decoy
        best = 0
        enemies = hero.findEnemies()
        self.best_target = None
        self.best_target_distance = 9999
        self.enemy_hero = [e for e in hero.findEnemies() if e.id in ["Hero Placeholder", "Hero Placeholder 1"]][0]

        if self.enemy_hero:
            self.best_target = self.enemy_hero
            self.best_target_distance = hero.distanceTo(self.best_target)

        door = hero.findNearest(hero.findByType('door'))
        if door:
            self.best_target = door
            self.best_target_distance = hero.distanceTo(door)

        if (not (self.best_target)):
            for enemy in enemies:
                if enemy.type in self.excludeType:
                    continue
                distance = hero.distanceTo(enemy)
                current = enemy.maxHealth * 10 / distance
                # hero.debug(enemy.id,enemy.type, current)
                if (best > current):
                    best = current
                    self.best_target = enemy
                    self.best_target_distance = distance

        if (not (self.best_target)):
            self.best_target = hero.findNearestEnemy()
            if self.best_target:
                self.best_target_distance = hero.distanceTo(self.best_target)
            else:
                self.best_target = None

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
            self.moveTo(nearestItem.pos)

    def attack(self):
        if self.best_target is not None:
            if hero.isReady("throw") and self.best_target.type != 'door':
                if self.best_target_distance < hero.throwRange:
                    hero.throw(self.best_target)
                else:
                    self.moveTo(self.best_target.pos)
            elif (hero.canCast('chain-lightning', self.best_target) and self.best_target_distance < 30):
                hero.cast('chain-lightning', self.best_target)
            elif (self.best_target_distance < hero.attackRange):
                hero.scattershot(self.best_target)
            else:
                self.moveTo(self.best_target.pos)
        else:
            if self.position == 'left':
                self.moveTo(Vector(50, 70))
            else:
                self.moveTo(Vector(110, 70))

    def _action(self):
        self.attack()

    def run(self):
        self.findTarget()
        self.summonTroops()
        self.commandTroops()
        self._action()


def onSpawn(e):
    while True:
        enemy = hero.findNearestEnemy()  # todo: list of closest
        if enemy and pet.isReady("chase") and enemy.maxHealth < enemy.maxHealth / 10:
            pet.chase(enemy)
        # Find and fetch a "potion":
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)


pet.on('spawn', onSpawn)
game = Game()
while True:
    game.run()
