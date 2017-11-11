# https://codecombat.com/play/level/table-scraps

# Feed the wolf pop to earn it's trust.
# Munchkins are making their rounds with food scraps
# Stop them and grab the food!

while True:
    hero.moveDown()
    hero.moveRight(2)
    # Attack the munchkin
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)    
    # Pick up the food    
    item = hero.findByType('cow')[0]
    hero.pickUpItem(item)
    hero.moveUp(2)
    hero.moveLeft(2)
    # Return to the wolf
    hero.moveDown()
    # Drop your item
    hero.dropItem()
