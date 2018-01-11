while (True):
    enemy = hero.findNearestEnemy()
    # Attack only skeletons AND if they are on the "ogres" team.
    if enemy and enemy.team == "ogres" and enemy.type == "skeleton":
        hero.attack(enemy)

    item = hero.findNearestItem()
    if hero.health < hero.maxHealth / 7 and item and item.type == 'potion':
        hero.move(item.pos)
        # Take only the "potion" type AND when your health less than quarter of the maxHealth.
