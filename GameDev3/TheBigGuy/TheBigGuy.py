# Game settings, goals and variables.
game.scoutInterval = 3
game.scoutSpawnTime = 0
game.ogreInterval = 5
game.ogreSpawnTime = 2
game.ogresDefeated = 0
ui.track(game, "ogresDefeated")
ogreGoal = game.addManualGoal("Defeat 5 big ogres.")
scaleGoal = game.addManualGoal("Grow twice.")

# Spawn an aggressive unit at a random point.
def spawnRandomXY(type):
    x = game.randomInteger(12, 68)
    y = game.randomInteger(12, 56)
    unit = game.spawnXY(type, x, y)
    unit.behavior = "AttacksNearest"

# This counts defeated ogres.
def onDefeat(event):
    game.ogresDefeated += 1

game.setActionFor("ogre", "defeat", onDefeat)

# The hero.
hero = game.spawnHeroXY("goliath", 40, 34)
hero.attackDamage = 20

# This tracks the hero's health and acts for that.
def onUpdateHero(event):
    unit = event.target
    # If the hero's health less than a third.
    if unit.health < unit.maxHealth / 3:
        # Increase the health, size and damage.
        unit.maxHealth *= 1.1
        unit.health = unit.maxHealth
        unit.scale *= 1.1
        unit.attackDamage *= 1.1
        unit.say("SMASH!")

# Assign the "update" handler with hero.on.
hero.on("update", onUpdateHero)

# This function checks spawn timers.
def checkTimers():
    if game.time > game.scoutSpawnTime:
        spawnRandomXY("scout")
        game.scoutSpawnTime += game.scoutInterval
    if game.time > game.ogreSpawnTime:
        spawnRandomXY("ogre")
        game.ogreSpawnTime += game.ogreInterval

# This function checks the goal states.
def checkGoals():
    if hero.scale >= 2:
        scaleGoal.success = True
    if game.ogresDefeated >= 5:
        ogreGoal.success = True

# This is the main game loop.
def onUpdateGame(event):
    # Call checkTimers and checkGoals functions:
    checkTimers()
    checkGoals()
    pass

# Assign the "update" handler with game.on.
game.on("update", onUpdateGame)
