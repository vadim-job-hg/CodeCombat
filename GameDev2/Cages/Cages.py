# https://codecombat.com/play/level/cages?
# Destroy fences and defeat bosses and generators.

# Enemies.
ogre1 = game.spawnXY("ogre", 12, 18)
ogre1.behavior = "AttacksNearest"
ogre2 = game.spawnXY("ogre", 68, 50)
ogre2.behavior = "AttacksNearest"

munchkinGenerator = game.spawnXY("generator", 12, 50)
munchkinGenerator.spawnAI = "Scampers"
munchkinGenerator.spawnType = "munchkin"

scoutGenerator = game.spawnXY("generator", 68, 12)
scoutGenerator.spawnAI = "Scampers"
scoutGenerator.spawnType = "scout"

# The fences which we will destroy later.
leftFence = game.spawnXY("fence", 26, 14)
rightFence = game.spawnXY("fence", 54 , 50)

player = game.spawnHeroXY("knight", 40, 34)
player.maxSpeed = 16
player.attackDamage = 20

# The global counters.
game.scoutsSpawned = 0
game.munchkinsSpawned = 0
game.bossesDefeated = 0
ui.track(game, "scoutsSpawned")
ui.track(game, "munchkinsSpawned")
ui.track(game, "bossesDefeated")

bossesGoal = game.addManualGoal("Defeat 2 big ogres.")

def onSpawn(event):
    unit = event.target
    if unit.type == "scout":
        game.scoutsSpawned += 1
    if game.scoutsSpawned >= 5:
        # Defeat scoutGenerator with the "defeat" method.
        scoutGenerator.defeat()
        # Destroy the right fence with the "destroy" method.
        rightFence.destroy()
        pass
    if unit.type == "munchkin":
        game.munchkinsSpawned += 1
    if game.munchkinsSpawned >= 3:
        # Defeat munchkinGenerator.
        munchkinGenerator.defeat()
        # Destroy the left fence.
        leftFence.destroy()
        pass

def onDefeat(event):
    unit = event.target
    if unit.type == "ogre":
        # Increase bossesDefeated counter by 1:
        game.bossesDefeated +=1
        pass

game.setActionFor("munchkin", "spawn", onSpawn)
game.setActionFor("scout", "spawn", onSpawn)
game.setActionFor("ogre", "defeat", onDefeat)

while True:
    if game.bossesDefeated >= 2:
        bossesGoal.success = True
