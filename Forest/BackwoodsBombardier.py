# http://codecombat.com/play/level/backwoods-bombardier
# The pos property is an object with x and y properties.
# pos.x is a number representing the horizontal position on the map
# pos.y is a number representing the vertical position on the map
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        x = enemy.pos.x
        y = enemy.pos.y
        # say the x and y position separated by a comma
        hero.say(x + ',' + y)
    else:
        hero.say("Cease Fire!")
