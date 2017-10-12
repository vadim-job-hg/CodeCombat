# https://codecombat.com/play/level/game-of-coins-iteration-3
# The game layout and items. Scroll down.
game.spawnXY("forest", 16, 16)
game.spawnXY("forest", 32, 16)
game.spawnXY("forest", 48, 16)
game.spawnXY("forest", 64, 16)
game.spawnXY("forest", 16, 32)
game.spawnXY("forest", 32, 32)
game.spawnXY("forest", 48, 32)
game.spawnXY("forest", 64, 32)
game.spawnXY("forest", 16, 48)
game.spawnXY("forest", 32, 48)
game.spawnXY("forest", 48, 48)
game.spawnXY("forest", 64, 48)

game.spawnXY("bronze-coin", 16, 8)
game.spawnXY("bronze-coin", 24, 8)
game.spawnXY("bronze-coin", 32, 8)
game.spawnXY("bronze-coin", 48, 8)
game.spawnXY("bronze-coin", 56, 8)
game.spawnXY("bronze-coin", 64, 8)
game.spawnXY("bronze-coin", 72, 8)

game.spawnXY("bronze-coin", 8, 16)
game.spawnXY("bronze-coin", 24, 16)
game.spawnXY("bronze-coin", 40, 16)
game.spawnXY("bronze-coin", 56, 16)
game.spawnXY("bronze-coin", 72, 16)

game.spawnXY("bronze-coin", 8, 24)
game.spawnXY("bronze-coin", 16, 24)
game.spawnXY("bronze-coin", 24, 24)
game.spawnXY("bronze-coin", 32, 24)
game.spawnXY("bronze-coin", 40, 24)
game.spawnXY("bronze-coin", 48, 24)
game.spawnXY("bronze-coin", 56, 24)
game.spawnXY("bronze-coin", 64, 24)
game.spawnXY("bronze-coin", 72, 24)

game.spawnXY("bronze-coin", 24, 32)
game.spawnXY("bronze-coin", 56, 32)

game.spawnXY("bronze-coin", 8, 40)
game.spawnXY("bronze-coin", 16, 40)
game.spawnXY("bronze-coin", 24, 40)
game.spawnXY("bronze-coin", 32, 40)
game.spawnXY("bronze-coin", 40, 40)
game.spawnXY("bronze-coin", 48, 40)
game.spawnXY("bronze-coin", 56, 40)
game.spawnXY("bronze-coin", 64, 40)
game.spawnXY("bronze-coin", 72, 40)

game.spawnXY("bronze-coin", 8, 48)
game.spawnXY("bronze-coin", 24, 48)
game.spawnXY("bronze-coin", 40, 48)
game.spawnXY("bronze-coin", 56, 48)
game.spawnXY("bronze-coin", 72, 48)

game.spawnXY("bronze-coin", 8, 56)
game.spawnXY("bronze-coin", 16, 56)
game.spawnXY("bronze-coin", 24, 56)
game.spawnXY("bronze-coin", 32, 56)
game.spawnXY("bronze-coin", 48, 56)
game.spawnXY("bronze-coin", 56, 56)
game.spawnXY("bronze-coin", 64, 56)
game.spawnXY("bronze-coin", 72, 56)

game.spawnXY("mushroom", 40, 8)
game.spawnXY("mushroom", 8, 32)
game.spawnXY("mushroom", 72, 32)
game.spawnXY("mushroom", 40, 56)

game.score = 1000
ui.track(game, "time")
ui.track(game, "score")
game.addCollectGoal()
# Enemies mean that we need a survive goal:
game.addSurviveGoal()

hero = game.spawnHeroXY("knight", 8, 8)
hero.maxSpeed = 30

def onCollect(event):
    player = event.target
    item = event.other
    if item.type == "coin":
        game.score += 1
    if item.type == "mushroom":
        game.score += 5

hero.on("collect", onCollect)

# Spawn the monster generator in the center:
munchkinSpawner = game.spawnXY("generator", 40, 32)
# The generator should spawn "scout" ogres:
munchkinSpawner.spawnType = "scout"
# Set the spawn delay greater than the default one:
munchkinSpawner.spawnDelay = 40

# The function configure new spawned ogres.
def onSpawn(event):
    unit = event.target
    unit.maxSpeed = 8
    # The enemy attack damage should be greater
    # or equal the hero's maximum health.
    unit.attackDamage = hero.maxHealth

# Set the event handler "scout"s' "spawn" event.


def checkTimeScore():
    game.score -= 0.5
    if game.score < 0:
        game.score = 0

while True:
    checkTimeScore()
