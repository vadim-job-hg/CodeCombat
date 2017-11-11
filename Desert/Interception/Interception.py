# http://codecombat.com/play/level/interception
# Protect the nearby peasant long enough to gather all the coins!
# Move to the point between their position and the tower's position!

while True:
    enemy = hero.findNearestEnemy()
    friend = hero.findNearest(hero.findFriends())
    # Find the point between the enemy's position and your friend's position.
    # Check the guide if you need more help!
    x = (enemy.pos.x + friend.pos.x) / 2
    y = (enemy.pos.y + friend.pos.y) / 2
    hero.move({'x': x, 'y': y})
