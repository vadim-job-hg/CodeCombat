# https://codecombat.com/play/level/chase-them

# Defeat the ogres and cure the hero.

# The pet is your only hope.
def onSpawn(e):
    while True:
        enemy = pet.findNearestByType("munchkin")
        if enemy and pet.isReady("chase"):
            pet.chase(enemy)
        # Find and fetch a "potion":
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)

# Assign "onSpawn" handler on the "spawn" event:
pet.on('spawn', onSpawn)
