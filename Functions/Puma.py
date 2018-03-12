def onSpawn(e):
    while True:
        enemy = hero.findNearestEnemy()  # todo: list of closest
        if enemy and pet.isReady("chase") and enemy.maxHealth < enemy.maxHealth / 10:
            pet.chase(enemy)
        # Find and fetch a "potion":
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)


pet.on('spawn', onSpawn)