# Make your own game by changing the code below!
# Spawn a maze. Change the number for a different maze!
game.spawnMaze(1)

# Spawn a hero with spawnHeroXY()
game.spawnHeroXY("raider", 28, 60)

# Add at least one goal!
game.addCollectGoal()
game.addDefeatGoal()
game.addSurviveGoal()

# Spawn some things to collect!
game.spawnXY("gem", 28, 27)
# You need a key to collect a locked chest.
game.spawnXY("locked-chest", 44, 28)
game.spawnXY("silver-key", 43, 60)
game.spawnXY("potion-medium", 60, 12)

# Spawn some enemies!
game.spawnXY("munchkin", 43, 43)
game.spawnXY("munchkin", 28, 19)
# Ogre Spear Throwers have a ranged attack!
game.spawnXY("thrower", 48, 28)
# This gargoyle shoots fire!
game.spawnXY("fire-spewer", 37, 12)
