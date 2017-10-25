# https://codecombat.com/play/level/dont-touch-them
# Use manual goals to control which ogres to defeat.

# Scouts are aggressive and munchkins are just walking.
scoutGenerator1 = game.spawnXY("generator", 12, 12)
scoutGenerator1.spawnType = "scout"
scoutGenerator1.spawnAI = "AttacksNearest"

scoutGenerator2 = game.spawnXY("generator", 68, 56)
scoutGenerator2.spawnType = "scout"
scoutGenerator2.spawnAI = "AttacksNearest"

munchkinGenerator1 = game.spawnXY("generator", 12, 56)
munchkinGenerator1.spawnType = "munchkin"
munchkinGenerator1.spawnAI = "Scampers"

munchkinGenerator2 = game.spawnXY("generator", 68, 12)
munchkinGenerator2.spawnType = "munchkin"
munchkinGenerator2.spawnAI = "Scampers"

player = game.spawnHeroXY("duelist", 40, 34)
player.maxHealth = 1000
player.attackDamage = 20
player.maxSpeed = 20

# There are our goals.
spawnMunchkinsGoal = game.addManualGoal("Let 6 munchkins spawn.")
dontTouchGoal = game.addManualGoal("Don't attack munchkins.")
defeatScoutsGoal = game.addManualGoal("Defeat 6 scouts.")
# Those varaibles are used to count new and defeated ogres.
game.spawnedMunchkins = 0
game.defeatedScouts = 0
ui.track(game, "spawnedMunchkins")
ui.track(game, "defeatedScouts")

def onSpawn(event):
    game.spawnedMunchkins += 1

def onDefeat(event):
    unit = event.target
    if unit.type == "scout":
        game.defeatedScouts += 1
    if unit.type == "munchkin":
        # The goal is failed.
        dontTouchGoal.success = False
        player.say("Oops.")

def checkGoals():
    # If game.defeatedScouts is greater or equal to 6:
    if game.defeatedScouts == 6:
        # Set scoutGoal.defeatScoutsGoal to True.
        defeatScoutsGoal.success = True
    # If game.spawnedMunchkins is greater or equal to 6:
    # Set scoutGoal.spawnMunchkinsGoal to True.
    if game.spawnedMunchkins >= 6:
        spawnMunchkinsGoal.success = True
    # If both goals are completed.
    if spawnMunchkinsGoal.success:
        if defeatScoutsGoal.success:
            # Set scoutGoal.dontTouchGoal to True.
            dontTouchGoal.success = True
            pass

game.setActionFor("munchkin", "spawn", onSpawn)
game.setActionFor("munchkin", "defeat", onDefeat)
game.setActionFor("scout", "defeat", onDefeat)

while True:
    checkGoals()
