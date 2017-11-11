def onSpawn(event):
    remainingPeasants = 3
    while remainingPeasants > 0:
        pet.moveXY(40, 55)
        peasant = pet.findNearestByType("peasant")
        if peasant:
            pet.carryUnit(peasant, 40, 34)
            remainingPeasants -= 1
    enemy = pet.findNearestByType('munchkin')
    if enemy:
        pet.carryUnit(enemy, 40, 19)
pet.on("spawn", onSpawn)

while True:
    enemy = None
    enemies = hero.findEnemies()
    for en in enemies:
        if en.pos.x>32 and en.pos.x<48:
            enemy = en
            break
    if enemy:
        hero.attack(enemy)
