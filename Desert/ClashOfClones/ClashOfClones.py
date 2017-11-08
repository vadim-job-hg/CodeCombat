hero.moveXY(68, 78)
back = 0
while True:
    enemys = hero.findEnemies()
    index = 0
    closest_soldier = None
    soldier_dist = 999
    closest_archer = None
    archer_dist = 999
    closest = None
    dist = 999
    while (index < len(enemys)):
        distance = hero.distanceTo(enemys[index])
        if (enemys[index].health > 0 and enemys[index].type != "sand-yak"):
            if (enemys[index].type == 'archer' and distance < archer_dist):
                archer_dist = distance
                closest_archer = enemys[index]
            if (enemys[index].type == 'soldier' and distance < soldier_dist):
                soldier_dist = distance
                closest_soldier = enemys[index]
            if (distance < dist):
                soldier_dist = dist
                closest = enemys[index]
        index += 1
    if (closest_soldier and soldier_dist < 10):
        enemy = closest_soldier
    elif (closest_archer and archer_dist < 20):
        enemy = closest_archer
    else:
        enemy = closest
    if (enemy):
        if (hero.health < hero.maxHealth / 2.5 and back == 0):
            hero.moveXY(40, 85)
            back = 1
        elif (hero.health < hero.maxHealth / 5 and back == 1):
            hero.moveXY(40, 85)
            back = 2
        elif (hero.isReady("jump") and hero.distanceTo > 15):
            hero.jumpTo(enemy.pos)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        elif (hero.isReady("cleave")):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
