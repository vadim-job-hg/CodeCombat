# https://codecombat.com/play/level/form-up
# Those soldiers before the gate are new recruits aren't trained.
# We should form up them by their height.
# Their 'health' property is proportional to their height.
# Form up them from the smallest to the biggest (from left to right).
# Command those 8 recruits to move on the marks in the right order.

# This function return coordinates of the i-th mark.
def markPos(i):
    return {"x": 12 + i * 8, "y": 12}

# This function return the list of soldiers who should be sorted.
def findUnplacedSoldiers():
    friends = hero.findFriends()
    result = []
    for friend in friends:
        # Recruits' actions are readable.
        if 18 < friend.pos.y and friend.pos.y  < 30 and friend.action == "idle":
            result.append(friend)
    return result

# This function should return the unit with the least health.
def minHealthUnit(units):
    min = 999
    cur = None
    for unit in units:
        if unit.health<min:
            min = unit.health
            cur = unit
    return cur
    # Write this function to use it for the sorting.


# Soldiers who should be sorted.
recruits = findUnplacedSoldiers()
markIndex = 0

# While there are soldiers who aren't in the position.
while len(recruits):
    hero.say(len(recruits) + " recruits aren't in the positions.")
    # Find the recruit with the minimum health.
    soldier = minHealthUnit(recruits)
    # Command him move the mark (use 'markPos' function and 'markIndex').
    pos = markPos(markIndex)
    hero.command(soldier, 'move', pos)
    # Increase markIndex by 1.
    markIndex = markIndex+1
    # Update the list of soldiers who should be sorted - 'recruits'.
    recruits = findUnplacedSoldiers()
