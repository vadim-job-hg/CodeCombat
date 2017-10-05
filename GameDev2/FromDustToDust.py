# https://codecombat.com/play/level/from-dust-to-dust
# Block passages with forest tiles.
# Then destroy them when the player defeats some ogres.

# Set up the hero.
hero = game.spawnHeroXY("duelist", 6, 34)
hero.attackDamage = 25
hero.maxHealth = 400
hero.health = 400
hero.maxSpeed = 15
# Player should pass through the forest.
game.addMoveGoalXY(76, 34)

# Set up enemies.
munchkinSpawner = game.spawnXY("generator", 16, 56)
munchkinSpawner.spawnType = "munchkin"
munchkinSpawner.spawnDelay = 3
scoutSpawner = game.spawnXY("generator", 40, 10)
scoutSpawner.spawnType = "scout"
scoutSpawner.spawnDelay = 5

# Those forest tiles should block passages.
passageForest1 = game.spawnXY("forest", 28, 34)
# Create the second forest and block the second passage:
passageForest2 = game.spawnXY("forest", 52, 34)

ui.track(game, "defeated")

def onDefeat(event):
    defeated = event.target
    game.defeated += 1
    # When 5 ogres are defeated.
    if game.defeated == 5:
        # No enemies behind!
        munchkinSpawner.die()
        # We need to clear the passage to the next zone.
        passageForest1.destroy()
    # When 10 ogres are defeated:
    if game.defeated == 10:
        # Ruin the scout generator:
        scoutSpawner.die()
        # Clear the second forest passage.
        passageForest2.destroy()
# Set "defeat" event handler for "scout"s and "munchkin"s.
game.setActionFor("scout", "defeat", onDefeat)
game.setActionFor("munchkin", "defeat", onDefeat)
# Beat the game!

