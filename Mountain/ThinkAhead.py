# http://codecombat.com/play/level/think-ahead
# You need to distract "Big Bertha" until you special squad arrives.
# The cannon always shoots at the pair of soldiers closest to each other.
# We can predict which pair of soldiers in danger and protect them.

# This function should find the pair of units with the minimum distance between them.
def findNearestPair(units):
    # These variables are used to store comparable value and results.
    minDistance = 9001
    nearestPair = ["Nobody", "Nobody"]
    # You need to check and compare all pairs of units.
    # Iterate all units with indexes 'i' from 0 to 'len(units)-1'.
    for i in range(0, len(units)):
        for j in range(i + 1, len(units)):
            # Use an additional loop through indexes 'j' from 'i+1' to 'len(units)'.

            # Find the distance between the i-th and j-th units.
            distance = units[i].distanceTo(units[j])
            # If the distance less than 'minDistance':
            if distance < minDistance:
                # Reassign 'minDistance' with the new distance.
                minDistance = distance
                # Reassign 'nearestPair' to the names of the current pair of units.
                nearestPair = [units[i].id, units[j].id]
    return nearestPair


while True:
    soldiers = hero.findByType("soldier")
    # We know when the cannon shoots.
    if hero.now() % 8 == 5:
        pairOfNames = findNearestPair(soldiers)
        # Say the soldier's names and wizards will protect them.
        hero.say(pairOfNames[0] + " " + pairOfNames[1])
