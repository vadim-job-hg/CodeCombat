# https://codecombat.com/play/level/uneasy-truce
# Summon one soldier for every ogre to the south of you!
# Don't count the ogres to the north!

# Accept an array of units as the parameter.
# Return only the units to the south of the hero.
def findSouthernUnits(units):
    southernUnits = []
    for unit in units:
        if unit.pos.y < hero.pos.y:
            # Add the unit to the array with: append()
            southernUnits.append(unit)
    return southernUnits


while True:
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    # Use findSouthernUnits to get enemies to the south.
    ogres = findSouthernUnits(enemies)
    # If there are more ogres south of you than friends.
    if(len(ogres)>len(friends)):
        # Then summon another "soldier".
        hero.summon("soldier")
