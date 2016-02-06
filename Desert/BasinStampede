#http://codecombat.com/play/level/basin-stampede
# Uh oh, a stampede! Use your cunning to make it to the oasis.

loop:
    enemy = self.findNearestEnemy()
    xPos = self.pos.x + 10
    yPos = 17
    if enemy:
        # You only need to shift up/down 1m to dodge the yaks!
        if enemy.pos.y > 17:
            # If the Yak is above you, adjust yPos downwards!
            yPos = 10
            pass
        elif enemy.pos.y <= 17:
            # If the Yak is below you, adjust yPos upwards!
            yPos = 25
            pass
    self.moveXY(xPos, yPos)
