# http://codecombat.com/play/level/crossroads
# Use fire-traps to defeat the ogres attacking the trading post.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.pos.x < 25:
            # If the enemy is to the left, build a fire-trap to the left.
            hero.buildXY("fire-trap", 25, 34)
            hero.moveXY(40, 34)
            pass
        elif enemy.pos.x > 55:
            # If the enemy is to the right, build a fire-trap to the right.
            hero.buildXY("fire-trap", 55, 34)
            hero.moveXY(40, 34)
            pass
        elif enemy.pos.y < 20:
            # If the enemy is below the hero, build a fire-trap below.
            hero.buildXY("fire-trap", 40, 20)
            hero.moveXY(40, 34)
            pass
        elif enemy.pos.y > 50:
            # If the enemy is above the hero, build a fire-trap above.
            hero.buildXY("fire-trap", 40, 50)
            hero.moveXY(40, 34)
            pass
    hero.moveXY(40, 34)
