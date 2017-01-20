# https://codecombat.com/play/level/game-grove
# Make your own game by changing the code below!
# Spawn a maze. Change the number for a different maze!
game.spawnMaze(1)

# Spawn a hero with spawnHeroXY()
game.spawnHeroXY(28, 60)

# Add at least one goal!
game.addCollectGoal()
game.addDefeatGoal()
game.addSurviveGoal()

# Add some things to collect!
game.spawnXY("gem", 28, 27)
game.spawnXY("locked-chest", 44, 28)
game.spawnXY("silver-key", 43, 60)
game.spawnXY("potion-medium", 60, 12)

# Add some enemies!
game.spawnXY("munchkin", 43, 43)
game.spawnXY("munchkin", 28, 19)
game.spawnXY("thrower", 48, 28)
game.spawnXY("horizontal-fire-trap", 37, 12)
