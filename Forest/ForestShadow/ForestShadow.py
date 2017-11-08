# https://codecombat.com/play/level/forest-shadow
# Big ogres can't see you in the forest.
# Kill only the small ogres in the forest.
# Collect coins and gems only.
# Don't leave the forest and don't eat/drink anything.

while True:
    # Find the nearest enemy.
    # Attack it only if its type is "thrower" or "munchkin".
    enemy = hero.findNearestEnemy()
    if enemy.type == 'thrower' or enemy.type == 'munchkin':
        hero.attack(enemy)
    # Find the nearest item.
    # Collect it only if its type is "gem" or "coin".
    item = hero.findNearestItem()
    if item.type == 'gem' or item.type == 'coin':
        hero.moveXY(item.pos.x, item.pos.y)
    pass
