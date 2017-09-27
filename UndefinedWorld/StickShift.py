# https://codecombat.com/play/level/stick-shift
# Now you can create a custom goal for your game!

# Spawn a few scouts, a boss, and a maze.
game.spawnMaze(5)
game.spawnXY("scout", 60, 58)
game.spawnXY("scout", 28, 29)
game.spawnXY("scout", 61, 24)
ogref = game.spawnXY("ogre-f", 60, 12)

# Spawn and configure the hero.
hero = game.spawnHeroXY("captain", 12, 56)
hero.maxHealth = 550
hero.maxSpeed = 10
hero.attackDamage = 25

# Spawn a munchkin generator.
generator = game.spawnXY("generator", 41, 13)
generator.spawnDelay = 5
generator.spawnType = "munchkin"

# Survive goal.
game.addSurviveGoal()
game.spawnXY("potion-medium", 28, 12)

# addManualGoal adds an incomplete goal with a description
# The description will be shown to players.
# NOTE that we save it in a variable!
scoutGoal = game.addManualGoal("Defeat all scouts")

# Use addManualGoal to add a goal to defeat the boss
# Save it in a variable called bossGoal
bossGoal = game.addManualGoal("Defeat the Boss")

# Enemy Behavior
def onSpawn(event):
    unit = event.target
    while True:
        enemy = unit.findNearestEnemy()
        if enemy:
            unit.attack(enemy)

game.setActionFor("scout", "spawn", onSpawn)
game.setActionFor("ogre", "spawn", onSpawn)

# Count how many scouts are defeated.
scoutsDefeated = 0

# Update our manual goals whenever an enemy is defeated.
# This is an example of an algorithm using if-statements.
def onDefeat(event):
    unit = event.target
    if unit.type == "scout":
        scoutsDefeated += 1
        hero.say("Scout down!")
    if scoutsDefeated >= 3:
        # Set scoutGoal.success to True to mark it complete.
        scoutGoal.success = True
        hero.say("All Scouts down!")
    if unit.type == "ogre":
        # Set the bossGoal.success to True
        bossGoal.success=True
        hero.say("Defeated the big boss!")
    if bossGoal.success and scoutGoal.success:
        hero.say("Job's done!")

# Assign the onDefeat handler to the ogres" "defeat"
# NOTE that munchkins don't count toward success!
game.setActionFor("scout", "defeat", onDefeat)
game.setActionFor("ogre", "defeat", onDefeat)
