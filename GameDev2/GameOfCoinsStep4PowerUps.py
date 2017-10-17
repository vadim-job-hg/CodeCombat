# https://codecombat.com/play/level/game-of-coins-step-4-power-ups?
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
# The duration of power-ups.
game.powerDuration = 4
# The time until a power-up runs out. Used for UI.
game.powerTime = 0
# The time a power-up expires. Used internally.
game.powerEndTime = 0
ui.track(game, "time")
ui.track(game, "score")
# Add ui for game.powerTime:


game.addCollectGoal()
game.addSurviveGoal();

hero = game.spawnHeroXY("knight", 8, 8)
hero.maxSpeed = 30

# The function make the hero big and strong.
def powerHeroUp():
    hero.scale = 2
    hero.attackDamage = 100
    game.powerEndTime = game.time + game.powerDuration

# The function return the hero in the normal state.
def powerHeroDown():
    hero.scale = 1
    hero.attackDamage = 1

def onCollect(event):
    player = event.target
    item = event.other
    if item.type == "bronze-coin":
        game.score += 1
    if item.type == "mushroom":
        game.score += 5
        # Use powerHeroUp to strengthen the hero:
        powerHeroUp()

def onCollide(event):
    player = event.target
    other = event.other
    # If other is a "scout" and the player's scale is 2:
    if other.type == 'scout' and player.scale==2:
        # Defeat the other with the defeat method:
        other.die()

hero.on("collect", onCollect)
# Assign the event handler for the hero's "collide" event:
hero.on("collide", onCollide)

generator = game.spawnXY("generator", 41, 31)
generator.spawnType = "scout"
generator.spawnDelay = 6;

def onSpawn(event):
    unit = event.target
    unit.maxSpeed = 8
    unit.attackDamage = hero.maxHealth
    while True:
        # Enemies run away from the big hero.
        if hero.scale == 2:
            unit.behavior = "RunsAway"
        else:
            unit.behavior = "AttacksNearest"

def onDefeat(event):
    # Increase game.score for defeated enemies:
    game.score +=1
    pass

game.setActionFor("scout", "spawn", onSpawn)
# Set the action for "scout"'s "defeat" event:
game.setActionFor("scout", "defeat", onDefeat)

def checkTimeScore():
    game.score -= 0.5
    if game.score < 0:
        game.score = 0

def checkPowerTimer():
    # Remaining power time.
    game.powerTime = game.powerEndTime - game.time
    if game.powerTime <= 0:
        game.powerTime = 0
        # If the hero's scale is 2:
        if hero.scale==2:
            # Use powerHeroDown to end the power-up.
            powerHeroDown()

# Lets combine all the time based functions.
def checkTimers():
    checkTimeScore()
    checkPowerTimer()

while True:
    checkTimers()

# Win the game.
