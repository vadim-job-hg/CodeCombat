# Двигайтесь вперед чтобы достичь оазиса,
# но двигайтесь назад, чтобы избежать яков поблизости.
loop:
    enemy = self.findNearestEnemy()
    if enemy and self.distanceTo(enemy) < 10:
        x = self.pos.x - 10
        y = self.pos.y
    else:
        x = self.pos.x + 10
        y = self.pos.y
    self.moveXY(x, y)
