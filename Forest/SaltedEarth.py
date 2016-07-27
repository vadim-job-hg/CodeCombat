# http://codecombat.com/play/level/salted-earth
# Ogres are attacking a nearby settlement!
# Be careful, though, for the ogres have sown the ground with poison.
# Gather coins and defeat the ogres, but avoid the burls and poison!

while True:
    enemy = hero.findNearestEnemy()
    if enemy.type == "munchkin" or enemy.type == "thrower":
        hero.attack(enemy)
    # item = hero.findNearestItem()
    item = hero.findNearest(hero.findItems())
    if (item.type == 'gem' or item.type == 'coin'):
        hero.move(item.pos)
        # Check the item type to make sure the hero doesn't pick up poison!
        # Look for types: 'gem' and 'coin'
