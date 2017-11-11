def waitFetch(event):
    potion = pet.findNearestByType("potion")
    if event.message == 'Fetch':
        pet.fetch(potion)
    else:
        pet.moveXY(54, 34)

pet.on("hear", waitFetch)
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(37, 34)
