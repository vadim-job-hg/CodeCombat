# https://codecombat.com/play/level/adventure-time
# game.time is the time that has passed in the game
game.spawnHeroXY("guardian", 10, 35)
game.addSurviveGoal()
game.addDefeatGoal(5)

def onSpawn(event):
    while True:
        unit = event.target
        enemy = unit.findNearestEnemy()
        if enemy:
            unit.attack(enemy)

game.setActionFor("munchkin", "spawn", onSpawn)

# game.time starts at zero, and counts upward in seconds
spawnTime = 0
while True:
    # spawnTime is the time we want to spawn at
    if game.time > spawnTime:
        # Spawn a "munchkin" at 60, 35
        game.spawnXY("munchkin", 35, 60)
        # Set spawnTime equal to game.time plus 2
        # so an enemy will spawn every 2 seconds.
        spawnTime = game.time + 2
