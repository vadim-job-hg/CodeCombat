# https://codecombat.com/play/level/game-of-coins-step-5-balance?
# Game parameters define the game difficulty.
# Δ Change the game parameters to balance the game.
# How long power-ups work (seconds).
POWER_DURATION = 10
# Score values for coins, mushrooms and ogres.
COIN_SCORE = 1
MUSHROOM_SCORE = 5
DEFEATED_SCORE = 10
# How fast the score is reduced.
TIME_SCORE = 0.5
# The player and ogres speed.
HERO_SPEED = 17
OGRE_SPEED = 2
# The ogre spawn delay (seconds).
SPAWN_DELAY = 10

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
game.powerDuration = POWER_DURATION
game.powerTime = 0
game.powerEndTime = 0
ui.track(game, "time")
ui.track(game, "score")
ui.track(game, "powerTime")
game.addCollectGoal()
game.addSurviveGoal();

hero = game.spawnHeroXY("knight", 8, 8)
hero.maxSpeed = HERO_SPEED

def powerHero(powerUp):
    if powerUp:
        hero.scale = 2
        hero.attackDamage = 100
        game.powerEndTime = game.time + game.powerDuration
    else:
        hero.scale = 1
        hero.attackDamage = 1

def onCollect(event):
    player = event.target
    item = event.other
    if item.type == "coin":
        game.score += COIN_SCORE
    if item.type == "mushroom":
        game.score += MUSHROOM_SCORE
        powerHero(True)

def onCollide(event):
    player = event.target
    other = event.other
    if other.type == "scout" and player.scale == 2:
        other.die()

hero.on("collect", onCollect)
hero.on("collide", onCollide)

generator = game.spawnXY("generator", 41, 31)
generator.spawnType = "scout"
generator.spawnDelay = SPAWN_DELAY;

def onSpawn(event):
    unit = event.target
    unit.maxSpeed = OGRE_SPEED
    unit.attackDamage = hero.maxHealth
    while True:
        if hero.scale == 2:
            unit.behavior = "RunsAway"
        else:
            unit.behavior = "AttacksNearest"

def onDefeat(event):
    game.score += DEFEATED_SCORE

game.setActionFor("scout", "spawn", onSpawn)
game.setActionFor("scout", "defeat", onDefeat)

def checkTimeScore():
    game.score -= TIME_SCORE
    if game.score < 0:
        game.score = 0

def checkPowerTimer():
    game.powerTime = game.powerEndTime - game.time
    if game.powerTime <= 0:
        game.powerTime = 0
        if hero.scale == 2:
            powerHero(False)

def checkTimers():
    checkTimeScore()
    checkPowerTimer()

while True:
    checkTimers()

# Win the game.
