# First, we need some borders.
game.spawnXY("forest", -4, 64)
game.spawnXY("forest", 4, 64)
game.spawnXY("forest", 12, 64)
game.spawnXY("forest", 20, 64)
game.spawnXY("forest", 28, 64)
game.spawnXY("forest", 36, 64)
game.spawnXY("forest", 44, 64)
game.spawnXY("forest", 52, 64)
game.spawnXY("forest", 60, 64)
game.spawnXY("forest", 68, 64)
game.spawnXY("forest", 76, 64)
game.spawnXY("forest", -4, 4)
game.spawnXY("forest", 4, 4)
game.spawnXY("forest", 12, 4)
game.spawnXY("forest", 20, 4)
game.spawnXY("forest", 28, 4)
game.spawnXY("forest", 36, 4)
game.spawnXY("forest", 44, 4)
game.spawnXY("forest", 52, 4)
game.spawnXY("forest", 60, 4)
game.spawnXY("forest", 68, 4)
game.spawnXY("forest", 76, 4)

# This moves "statical" objects.
def onUpdateStatic(event):
    thing = event.target
    # Each time frame we move them a little to the left:
    thing.pos.x -= 0.8
    # If thing's X coordinate is less than -4:
    if thing.pos.x<-4:
        # If thing's type is "forest":
        if thing.type=="forest":
            # Then set thing.pos.x to 84:
            thing.pos.x = 84
        # Otherwise destroy the thing:
        else:
            thing.destroy()

# Forest tiles are moving for the visual running effect.
game.setActionFor("forest", "update", onUpdateStatic)

# This spawns a fence on the right side.
def spawnRandomY(type):
    y = game.randomInteger(12, 56)
    spawn = game.spawnXY(type, 80, y)
    # Fences should move to the left.
    spawn.on("update", onUpdateStatic)

# This spawns several fences based on the game time.
def spawnFences():
    # One until 10 seconds, 2 until 20 seconds, etc.
    spawnNumber = 1 + (game.time / 10)
    while spawnNumber >= 1:
        spawnRandomY("fence")
        spawnNumber -= 1

# Setup the game, timers, UI, and goals.
game.spawnFenceTime = 0
ui.track(game, "time")
game.addSurviveGoal(20)

# Hero setup.
hero = game.spawnHeroXY("captain", 12, 34)
hero.maxSpeed = 20

# This checks hero collisions.
def onCollide(event):
    unit = event.target
    other = event.other
    if other.type == "fence":
        unit.defeat()

hero.on("collide", onCollide)

# Those functions define the game loop.
def checkHero():
    # The hero should be "statical" by X-axis.
    hero.pos.x = 20

def checkTimers():
    if game.time > game.spawnFenceTime:
        spawnFences()
        game.spawnFenceTime += 1

def onUpdateGame(event):
    checkHero()
    checkTimers()

game.on("update", onUpdateGame)
