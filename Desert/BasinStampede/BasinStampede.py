while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 10
    yPos = 17
    if enemy:
        if enemy.pos.y > 17:
            yPos = 10
        elif enemy.pos.y <= 17:
            yPos = 25
    hero.moveXY(xPos, yPos)
