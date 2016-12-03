# https://codecombat.com/play/level/agony-of-defeat
# The "defeat" event signals that a unit was defeated.
game.spawnHeroXY("captain", 40, 35)
game.addSurviveGoal()
game.addCollectGoal(8)

def onSpawn(event):
    while True:
        unit = event.target
        enemy = unit.findNearestEnemy()
        if enemy:
            unit.attack(enemy)

# When a unit is defeated, spawn a gold coin.
def onDefeat(event):
    unit = event.target
    # Set x to unit.pos.x, plus a number between -5 and 5
    x = unit.pos.x + game.randomInteger(-5, 5)
    # Set y to unit.pos.y, plus a number between -5 and 5
    y = unit.pos.y +game.randomInteger(-5,5)
    # Spawn a "gold-coin" at x, y
    hero.spawnXY("gold-coin", x, y)

game.setActionFor("munchkin", "spawn", onSpawn)
game.setActionFor("munchkin", "defeat", onDefeat)

spawnTime = 0
while True:
    if game.time > spawnTime:
        x = game.randomInteger(10, 70)
        y = game.randomInteger(10, 60)
        game.spawnXY("munchkin", x, y)
        spawnTime = game.time + game.randomInteger(5,10)
