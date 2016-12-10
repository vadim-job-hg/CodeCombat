#https://codecombat.com/play/level/safe-spot
# todo:
# Activate bombs and survive, then reach the dungeon enter.

# The function checks if numbers are almost equal.
def almostEqual(n1, n2):
    return abs(n1 - n2)


# The function checks that all
# thangs are on the same distance from the hero.
def allSameDistance(thangs):
    if len(thangs) == 0:
        return True
    # We can use any thang as an etalon.
    etalon = hero.distanceTo(thangs[0])
    # Iterate all thangs:
    for thang in thangs:
        # If the distance to the current thang
        # is not almost equal to the etalon:
        if not (almostEqual(hero.distanceTo(thang), etalon)):
            return False

    return True


bombs = hero.findEnemies()
for x in range(36, 45):
    for y in range(30, 39):
        hero.moveXY(x, y)
        if allSameDistance(bombs):
            # It's a safe spot. Rock'n'Roll!
            hero.say("HEEEEEEEEEY!!!")
            hero.moveXY(40, 58)

hero.say("Heh. Nothing.");
