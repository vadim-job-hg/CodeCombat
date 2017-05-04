# https://codecombat.com/play/level/throwing-fire
# Game objects can be configured by setting properties

# Don't change this, it sets up the game.
player = game.spawnHeroXY("knight", 40, 10)
game.addCollectGoal()
game.addSurviveGoal()

game.spawnXY("gem", 32, 55)
game.spawnXY("gem", 51, 55)

fs1 = game.spawnXY("fire-spewer", 12, 25)
fs2 = game.spawnXY("fire-spewer", 70, 30)
fs3 = game.spawnXY("fire-spewer", 12, 35)
fs4 = game.spawnXY("fire-spewer", 70, 40)

# Change fs1.direction to "vertical":
fs1.direction = "horizontal"

# Now set fs2.direction to "vertical":
fs2.direction = "vertical"
# Do the same for fs3 and fs4:
fs3.direction = "horizontal"
fs4.direction = "vertical"
# Now play the game and collect the gems!
