GAME_SPEED = 0.8
FENCE_INTERVAL = 1
GEM_INTERVAL = 1
GEM_SCORE = 5
WIN_TIME = 10
HERO_SPEED = 20
BASE_SPAWNS = 1

# ENVIROMENT
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


def onUpdateStatic(event):
    thing = event.target
    thing.pos.x -= GAME_SPEED
    if thing.pos.x < -4:
        if thing.type == "forest":
            thing.pos.x = 84
        else:
            thing.destroy()


game.setActionFor("forest", "update", onUpdateStatic)


def spawnRandomY(type):
    y = game.randomInteger(12, 56)
    spawn = game.spawnXY(type, 80, y)
    spawn.on("update", onUpdateStatic)


def spawnFences():
    spawnNumber = BASE_SPAWNS + (game.time / 10)
    while spawnNumber >= 1:
        spawnRandomY("fence")
        spawnNumber -= 1


## GAME, UI AND GOALS
game.spawnFenceTime = 0
game.spawnGemTime = 0.5
game.score = 0
game.topScore = db.get("topScore")
ui.track(game, "time")
ui.track(game, "score")
ui.track(game, "topScore")
goal = game.addManualGoal("Survive at least 30 seconds")

## HERO
hero = game.spawnHeroXY("captain", 12, 34)
hero.maxSpeed = HERO_SPEED


def onCollect(event):
    if event.other.type == "gem":
        game.score += GEM_SCORE


def onCollide(event):
    if event.other.type == "fence":
        event.target.defeat()


hero.on("collect", onCollect)
hero.on("collide", onCollide)


# GAME LOOP

def checkHero():
    # hero.moveXY(hero.pos.x + 1, hero.pos.y)
    if hero.health <= 0:
        gameOver()
    else:
        hero.pos.x = 12


def setTopScore():
    topScore = db.get("topScore")
    if game.score > game.topScore:
        db.set("topScore", game.score)


def gameOver():
    hero.on("update", onUpdateStatic)
    if game.time > WIN_TIME:
        goal.success = True
    else:
        goal.success = False
    setTopScore()


def checkSpawns():
    if game.time > game.spawnFenceTime:
        spawnFences()
        game.spawnFenceTime += FENCE_INTERVAL
    if game.time > game.spawnGemTime:
        spawnRandomY("gem")
        game.spawnGemTime += GEM_INTERVAL


def onUpdateGame(event):
    checkHero()
    checkSpawns()
    game.score += event.deltaTime


game.on("update", onUpdateGame)

