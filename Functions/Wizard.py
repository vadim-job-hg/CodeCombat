class Game:
    summonTypes = ['paladin']

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
        for enemy in enemies:
            distance = hero.distanceTo(enemy)
            current = enemy.maxHealth / distance
            if (best > current):
                best = current
                self.best_target = enemy
                self.best_target_distance = distance

        if (not (self.best_target)):
            self.best_target = hero.findNearestEnemy()
            self.best_target_distance = hero.distanceTo(self.best_target)

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
        hero.command(soldier, "defend", hero)

    def _commandPeasant(self, soldier):
        item = soldier.findNearestItem()
        if item:
            hero.command(soldier, "move", item.pos)

    def _commandPaladin(self, paladin):
        if (paladin.canCast("heal") and hero.health < hero.maxHealth):
            hero.command(paladin, "cast", "heal", hero)
        else:
            hero.command(paladin, "shield")

    def pickUpNearestItem(self, items):
        nearestItem = hero.findNearest(items)
        if nearestItem:
            moveTo(nearestItem.pos)

    def attack(self):
        if (hero.canCast('summon-burl', hero)):
            hero.cast('summon-burl')
        elif (hero.canCast('earthskin', hero)):
            hero.cast('earthskin', hero)
            self._earthskin = hero.now()
        elif (hero.canCast('raise-dead')):
            hero.cast('raise-dead')
        elif (hero.canCast('summon-undead')):  # todo: check for bodies
            hero.cast('summon-undead')
        # todo: mass targets
        elif self.best_target is not None:
            if (hero.canCast('fear', self.best_target) and self.best_target_distance < 25):
                hero.cast('fear', self.best_target)
            elif (hero.canCast('drain-life', self.best_target) and self.best_target_distance < 15):
                hero.cast('drain-life', self.best_target)
            # elif (hero.canCast('poison-cloud', self.best_target) and hero.distanceTo(self.best_target)<30):
            #    hero.cast('poison-cloud', self.best_target)
            elif (
                hero.canCast('chain-lightning', self.best_target) and hero.distanceTo(self.best_target_distance) < 30):
                hero.cast('chain-lightning', self.best_target)
            else:
                hero.attack(self.best_target)

    def run(self):
        self.findTarget()
        self.summonTroops()
        self.commandTroops()
        self.attack()


game = Game()
while True:
    game.run()
