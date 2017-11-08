# https://codecombat.com/play/level/disintegration-arrow
# Destroy at least 100 defeated ogres.

# It spawns and configures an archer.
def spawnArcher(x, y):
    archer = game.spawnXY("archer", x, y)
    archer.behavior = "Defends"
    archer.attackDamage = 20


# It spawns and configures an ogre.
def spawnMunchkin(x, y):
    ogre = game.spawnXY("munchkin", x, y)
    ogre.behavior = "AttacksNearest"


# Spawns some archers in a row.
def spawnArcherWall():
    spawnArcher(30, 12)
    spawnArcher(30, 23)
    spawnArcher(30, 34)
    spawnArcher(30, 45)
    spawnArcher(30, 56)


# Spawns an ogre wave with a random offset.
def spawnOgreWave():
    offset = game.randomInteger(-6, 6)
    spawnMunchkin(80, 16 + offset)
    spawnMunchkin(80, 22 + offset)
    spawnMunchkin(80, 28 + offset)
    spawnMunchkin(80, 34 + offset)
    spawnMunchkin(80, 40 + offset)
    spawnMunchkin(80, 46 + offset)
    spawnMunchkin(80, 52 + offset)


def onDefeat(event):
    unit = event.target
    # Increase the game defeated counter by 1.
    game.defeated += 1
    # Destroy the unit.
    unit.destroy()


# Set the event handler for 'munchkin' 'defeat' event.
game.setActionFor("munchkin", "defeat", onDefeat)

game.defeated = 0
game.spawnTime = 0
# The generic defeat goal can't work for our case.xxxx
goal = game.addManualGoal("Defeat 111 ogres")
ui.track(game, "defeated")


def checkSpawnTimer():
    if game.time > game.spawnTime:
        spawnOgreWave()
        game.spawnTime += 1


def checkGoal():
    # If the game defeated counter is greater than 111:
    if (game.defeated > 111):
        # Mark the goal as successfully completed.
        goal.success = True
    pass


spawnArcherWall()
while True:
    checkSpawnTimer()
    checkGoal()
