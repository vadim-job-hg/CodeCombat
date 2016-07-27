# http://codecombat.com/play/level/backwoods-bombardier
# The pos property is an object with x and y properties.
# pos.x is a number representing the horizontal position on the map
# pos.y is a number representing the vertical position on the map
loop:
enemy = self.findNearestEnemy()
if enemy:
    x = enemy.pos.x
    y = enemy.pos.y
    # say the x and y position separated by a comma
    self.say(x + ',' + y)
else:
    self.say("Cease Fire!")
