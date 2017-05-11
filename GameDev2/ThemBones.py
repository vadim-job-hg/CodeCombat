# https://codecombat.com/play/level/them-bones
# Generators spawn enemies over time.
# Skeletons are afraid of lightstones.

player = game.spawnHeroXY("champion", 15, 35)
player.attackDamage = 60
player.maxSpeed = 8

game.addSurviveGoal()
game.addDefeatGoal()

# Spawn a "generator"
game.spawnXY("generator", 20, 25)
# Spawn a "lightstone"
game.spawnXY("lightstone", 20, 25)
# Now beat your game!
