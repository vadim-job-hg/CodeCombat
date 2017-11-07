# https://codecombat.com/play/level/persistence-pays
# You can use a database to store persistent data.
# Persistent data stays the same between plays of your game!

generator = game.spawnXY("generator", 60, 40)
generator.spawnType = "munchkin"
player = game.spawnHeroXY("raider", 15, 15)
player.maxHealth = 80
player.attackDamage = 10
game.addSurviveGoal(20)

# db stands for database
# db.add(key, value) increments a value stored in the database.
# This adds 1 to the "plays" key in the database.
db.add("plays", 1)

# Show the number of people who play your game:
ui.track(db, "plays")

# Use ui.track to show the game's defeated property:
ui.track(game, 'defeated')
while True:
    db.set('defeated', game.defeated)
    # Use db.set(key, value) to store the value of
    # game.defeated in the database with the key "defeated"
