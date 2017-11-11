# Step 3 of creating a Pac-Man style arcade game.

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
# Lets simplify the game while we don't have power-ups.
game.addCollectGoal(10)
# Add a survive goal, since we have enemies now:
game.addSurviveGoal()

hero = game.spawnHeroXY("knight", 8, 8)
hero.maxSpeed = 32

def onCollect(event):
    player = event.target
    item = event.other
    if item.type == "bronze-coin":
        game.score += 1
    if item.type == "mushroom":
        game.score += 5

hero.on("collect", onCollect)

# Spawn a monster "generator" in the center:
munchkinSpawner = game.spawnXY("generator", 40, 32)
# Set the generator spawnType to “scout”.
munchkinSpawner.spawnType = "scout"
# Set the generator spawnDelay to something greater than 5
munchkinSpawner.spawnDelay = 60

# This function configures new spawned scouts.
def onSpawn(event):
    unit = event.target
    unit.maxSpeed = 1
    # The enemy attackDamage should be greater than
    # or equal to the hero's maxHealth.
    unit.attackDamage = hero.maxHealth

# Set the handler for "scout"s' "spawn" event to onSpawn
game.setActionFor("scout", "spawn", onSpawn)

def checkTimeScore():
    game.score -= 0.5
    if game.score < 0:
        game.score = 0

while True:
    checkTimeScore()

# Win the game.
