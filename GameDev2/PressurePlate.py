# https://codecombat.com/play/level/pressure-plate
# Learn to use X Marks as triggers!

# Set up the maze.
game.spawnMaze(3)
game.spawnXY("forest", 20, 45)
game.spawnXY("forest", 20, 28)
game.spawnXY("forest", 20, 58)
game.spawnXY("forest", 36, 60)
game.spawnXY("forest", 36, 44)
game.spawnXY("forest", 36, 13)

# Hero and goal.
hero = game.spawnHeroXY("knight", 60, 34)
goal = game.addManualGoal("Defeat 30 munchkins!")

# Fire cannons!
fire1 = game.spawnXY("fire-spewer", 27, 12)
fire2 = game.spawnXY("fire-spewer", 29, 12)
fire3 = game.spawnXY("fire-spewer", 11, 12)
fire4 = game.spawnXY("fire-spewer", 13, 12)
fire1.direction = "vertical"
fire2.direction = "vertical"
fire3.direction = "vertical"
fire4.direction = "vertical"
# NOTE Setting disabled to True stops the fire.
fire1.disabled = True
fire2.disabled = True
fire3.disabled = True
fire4.disabled = True

# These are our triggers.
# boneX will trigger fire.
boneX = game.spawnXY("x-mark-bones", 60, 50)
# stoneX will trigger munchkin spawns.
stoneX = game.spawnXY("x-mark-stone", 60, 22)

game.spawns = 0
game.defeated = 0
ui.track(game, "spawns")
ui.track(game, "defeated")

# Count defeated munchkins.
def onDefeat(event):
    game.defeated += 1

game.setActionFor("munchkin", "defeat", onDefeat)

# Spawns 2 munchkins every 0.25 seconds.
game.spawnTime = 0
game.spawnCooldown = 0.25

def spawnMunchkinsOverTime():
    if game.time >= game.spawnTime:
        m1 = game.spawnXY("munchkin", 11, 57)
        m2 = game.spawnXY("munchkin", 28, 57)
        m1.behavior = "Scampers"
        m2.behavior = "Scampers"
        # Count number of spawns.
        game.spawns += 2
        game.spawnTime = game.time + game.spawnCooldown

# Turn on fire if hero is near boneX
def checkBoneX():
    if boneX.distanceTo(hero) <= 1:
        hero.say("Firing!")
        fire1.disabled = False
        # Set disabled to False for the other cannons
        fire2.disabled = False
        fire3.disabled = False
        fire4.disabled = False
    else:
        fire1.disabled = True
        fire2.disabled = True
        fire3.disabled = True
        fire4.disabled = True

# Spawn munchkins if hero is near stoneX
def checkStoneX():
    pass
    # If the distance between stoneX and hero <= 1:
    if(stoneX.distanceTo(hero)<=1):
        # Call the spawnMunchkinsOverTime() function
        spawnMunchkinsOverTime()

def checkVictory():
    if game.defeated >= 30:
        pass
        # Set goal.success to True
        goal.success=True

# Main game loop.
while True:
    checkStoneX()
    checkBoneX()
    checkVictory()

