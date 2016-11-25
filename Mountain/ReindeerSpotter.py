# http://codecombat.com/play/level/reindeer-spotter
# This array contains the positions of the pens that we want to put the reindeer in.
penPositions = [{'x': 20, 'y': 24}, {'x': 28, 'y': 24}, {'x': 36, 'y': 24}, {'x': 44, 'y': 24}, {'x': 52, 'y': 24}]

# This array is used to track which reindeer (if any) is in each pen.
penOccupants = ['empty', 'empty', 'empty', 'empty', 'empty']

# And this array contains our reindeer.
friends = hero.findFriends()

# Figure out which reindeer are already in their pens.
for deerIndex in range(len(friends)):
    reindeer = friends[deerIndex]

    # Go through each position and see if it matches the reindeer's position.
    for penIndex in range(len(penPositions)):
        penPos = penPositions[penIndex]

        if penPos.x == reindeer.pos.x and penPos.y == reindeer.pos.y:
            # Put the reindeer's ID in the penOccupants array in slot penIndex.
            penOccupants[penIndex] = reindeer.id
            # break out of the inner loop here to avoid confusion.
            break;
            pass

# Tell Merek what's in each pen.
for occIndex in range(len(penOccupants)):
    # Tell Merek the pen index and the occupant.
    # Say something like "Pen 2 is empty" or "Pen 3 is Dasher"
    hero.say("Pen " + occIndex + " is " + penOccupants[occIndex])
    pass
