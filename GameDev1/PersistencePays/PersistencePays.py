generator = game.spawnXY("generator", 60, 40)
generator.spawnType = "munchkin"
player = game.spawnHeroXY("raider", 15, 15)
player.maxHealth = 80
player.attackDamage = 10
game.addSurviveGoal(20)
db.add("plays", 1)
ui.track(db, "plays")
ui.track(game, 'defeated')
while True:
    db.set('defeated', game.defeated)