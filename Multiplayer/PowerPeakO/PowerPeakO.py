def petLogic():
    # Add code to use your pet!
    # Move them to the power discs at the top of the map for powerups.
    while True:
        pet.moveXY(51, 74);
        item = pet.findNearestItem()
        if item:
            pet.fetch(item)


pet.on('spawn', petLogic)
while True:
    # Improve your hero's default code!
    # Move to the nearby power discs to spawn units to help or attack!

    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if hero.isReady('cleave'):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    elif item:
        hero.moveXY(item.pos.x, item.pos.y)