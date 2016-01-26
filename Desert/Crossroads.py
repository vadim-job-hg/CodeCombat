#http://codecombat.com/play/level/crossroads
# Use fire-traps to defeat the ogres attacking the trading post.

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        if enemy.pos.x < 25:
            # If the enemy is to the left, build a fire-trap to the left.
            self.buildXY("fire-trap",25, 34)
            self.moveXY(40, 34)
            pass
        elif enemy.pos.x > 55:
            # If the enemy is to the right, build a fire-trap to the right.
            self.buildXY("fire-trap", 55, 34)
            self.moveXY(40, 34)
            pass
        elif enemy.pos.y < 20:
            # If the enemy is below the hero, build a fire-trap below.
            self.buildXY("fire-trap",40, 20)
            self.moveXY(40, 34)
            pass
        elif enemy.pos.y > 50:
            # If the enemy is above the hero, build a fire-trap above.
            self.buildXY("fire-trap",40, 50)
            self.moveXY(40, 34)
            pass
    self.moveXY(40, 34)
