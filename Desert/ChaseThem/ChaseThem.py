def onSpawn(e):
    while True:
        enemy = pet.findNearestByType("munchkin")
        if enemy and pet.isReady("chase"):
            pet.chase(enemy)
        # Find and fetch a "potion":
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)
pet.on('spawn', onSpawn)
