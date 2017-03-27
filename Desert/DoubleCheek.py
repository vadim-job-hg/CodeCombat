# https://codecombat.com/play/level/double-cheek
# Kill at least 6 ogres on the left side.
# Then, collect at least 30 gold on the right.
# This variable is used for counting ogres.
defeatedOgres = 0;

# This loop is executed while "defeatedOgres" is less than 6.
while defeatedOgres < 6:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        defeatedOgres += 1
    else:
        hero.say("Ogres!")

# Move to the right part of the map.
hero.moveXY(49, 36)

# This loop is executed while you have less than 30 gold.
while hero.gold < 30:
    # Find and collect coins.
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
# Move to the exit.
hero.moveXY(76, 32)
