# https://codecombat.com/play/level/usual-day
# Kill munchkins, collect coins. Everything as usual.
# Use AND operator to check thang's existence and type in one statement.

while True:
    enemy = hero.findNearestEnemy()
    # The second operand after AND will only happen if the first one is true.
    if enemy and enemy.type == "munchkin":
        hero.attack(enemy);
    # Find the nearest item. Collect it if it exist and its type is "coin".
    item = hero.findNearestItem()
    if item and item.type == "coin":
        hero.moveXY(item.pos.x, item.pos.y);
