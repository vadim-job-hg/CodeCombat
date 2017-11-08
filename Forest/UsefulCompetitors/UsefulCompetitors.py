# http://codecombat.com/play/level/useful-competitors
# The coin field has been seeded with vials of deadly poison.
# Ogres are attacking, while their peons are trying to steal your coins!
# Let the peons pick up the poison, and only gather the coins and gems.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if not enemy.type is "peon":
            hero.attack(enemy)
    # item = hero.findNearestItem()
    item = hero.findNearestItem()
    if item and item.type != 'poison':
        hero.move(item.pos)
        # Gather the item only if it is not poison.
