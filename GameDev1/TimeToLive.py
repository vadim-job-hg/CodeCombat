# https://codecombat.com/play/level/time-to-live
# Pass an argument to addSurviveGoal() to specify a time.

# This means the player must survive for 20 seconds.
game.addSurviveGoal(20)

# Spawn a generator with spawnXY
# Remember to assign the spawned generator to a variable!
# Use the variable to configure the generator below.
generator = game.spawnXY("generator", 7, 10)
# Set the generator's spawnType to "munchkin"
generator.spawnType ="munchkin"
# Use spawnHeroXY to spawn a hero for the player.
# Remember to assign the spawned hero to a variable!
hero = game.spawnHeroXY("captain",69, 58)
# Set the hero's maxHealth to 100
hero.maxHealth = 100
# Set the hero's attackDamage to 10
hero.attackDamage = 10
# Play the game!

