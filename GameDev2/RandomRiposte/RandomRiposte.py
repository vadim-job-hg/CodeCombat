# https://codecombat.com/play/level/random-riposte
# Use game.randomInteger(min,max) to add randomness!
game.spawnHeroXY("knight", 40, 35)
game.addSurviveGoal()
game.addDefeatGoal(8)

def onSpawn(event):
    while True:
        unit = event.target
        enemy = unit.findNearestEnemy()
        if enemy:
            unit.attack(enemy)

game.setActionFor("munchkin", "spawn", onSpawn)

# Spawn an ogre every 2 seconds.
spawnTime = 0
while True:
    if game.time > spawnTime:
        # Spawn a "munchkin" at a random location
        # Set x to a random number between 10 and 70
        x = game.randomInteger(10, 70)
        # Set y to a random number between 10 and 60
        y = game.randomInteger(10,60)
        # Spawn a "munchkin" at x, y
        game.spawnXY('munchkin', x, y)
        # Spawn again in 0 through 4 seconds
        spawnTime = game.time + game.randomInteger(0,4)
