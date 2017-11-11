hero = game.spawnHeroXY(45, 45, "samurai")

spawner = game.spawnXY("generator", 50, 50)
spawner.spawnType = "munchkin"

ui.track(game, "time")

game.addSurviveGoal(20)

ui.track(game, "defeated")
hero.attackDamage = 20000
hero.maxSpeed = 50
spawner2 = game.spawnXY("generator", 43, 56)
spawner2.spawnType = "munchkin"
spawner2 = game.spawnXY("generator", 37, 43)
spawner2.spawnType = "munchkin"
