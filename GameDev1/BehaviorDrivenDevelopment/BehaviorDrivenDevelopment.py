# Assign behaviors to units with the behavior property.

skeleton1 = game.spawnXY("skeleton", 60, 50)
skeleton2 = game.spawnXY("skeleton", 60, 40)
skeleton3 = game.spawnXY("skeleton", 60, 30)
skeleton4 = game.spawnXY("skeleton", 60, 20)
skeleton5 = game.spawnXY("skeleton", 60, 10)

skeleton1.behavior = "Scampers"
skeleton2.behavior = "Scampers"
skeleton3.behavior = "Scampers"
# Assign "Scampers" to skeleton4.behavior
skeleton4.behavior = "Scampers"
# Assign "Scampers" to to skeleton5.behavior
skeleton5.behavior = "Scampers"

ogre1 = game.spawnXY("ogre", 70, 50)
ogre2 = game.spawnXY("ogre", 70, 30)
ogre3 = game.spawnXY("ogre", 70, 10)

ogre1.behavior = "AttacksNearest"
# Assign "AttacksNearest" to ogre2.behavior
ogre2.behavior = "AttacksNearest"
# Assign "AttacksNearest" to ogre3.behavior
ogre3.behavior = "AttacksNearest"

archer1 = game.spawnXY("archer", 10, 30)
# Assign "Defends" to archer1.behavior
archer1.behavior = "Defends"
# Don't need to change anything below here.
# But feel free to take a look!
player = game.spawnHeroXY("raider", 20, 30)
player.attackDamage = 10
game.addSurviveGoal()
game.addDefeatGoal()

game.spawnXY("forest", 40, 10)
game.spawnXY("forest", 40, 18)
game.spawnXY("forest", 40, 26)
game.spawnXY("forest", 40, 42)
game.spawnXY("forest", 40, 50)
game.spawnXY("forest", 40, 58)

game.spawnXY("lightstone", 30, 45)
game.spawnXY("lightstone", 30, 20)
game.spawnXY("lightstone", 30, 55)
game.spawnXY("lightstone", 30, 10)

game.spawnXY("potion-medium", 10, 50)
game.spawnXY("potion-medium", 10, 15)
