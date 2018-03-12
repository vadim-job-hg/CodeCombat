def onSpawn(event):
    while True:
        pet.moveXY(59, 20)
        pet.moveXY(100, 55)
        pet.moveXY(55, 75)
        pet.moveXY(21, 53)
        pet.moveXY(59, 22)
        pet.moveXY(hero.pos.x + 5, hero.pos.y + 5)
        pet.moveXY(hero.pos.x - 5, hero.pos.y - 5)


pet.on("spawn", onSpawn)