# https://codecombat.com/play/level/spinach-power
# Collect exactly no more than 7 spinach potions.
# With these potions you'll be strong enough to kill ogres.

potionCount = 0

# Use while with a condition to check the number of collected potions.
# Δ Wrap the next code block into while loop.
while potionCount != 7:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        potionCount += 1

# When the while loop is finished.
# Go and fight!.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

