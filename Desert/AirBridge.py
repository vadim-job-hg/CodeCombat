# https://codecombat.com/play/level/air-bridge
# Помоги крестьянам сбежать.

def onSpawn(event):
    # Нам нужно спасти трёх крестьян.
    remainingPeasants = 3
    while remainingPeasants > 0:
        # Займи правильную позицию.
        pet.moveXY(40, 55)
        peasant = pet.findNearestByType("peasant")
        if peasant:
            # Неси крестьян к центральному проходу.
            pet.carryUnit(peasant, 40, 34)
            remainingPeasants -= 1
    # Затем найди слабого огра и перенеси его к минам:
    enemy = pet.findNearestByType('munchkin')
    if enemy:
        pet.carryUnit(enemy, 40, 19)
pet.on("spawn", onSpawn)

# В бой!
while True:
    enemy = None
    enemies = hero.findEnemies()
    for en in enemies:
        if en.pos.x>32 and en.pos.x<48:
            enemy = en
            break
    if enemy:
        hero.attack(enemy)
