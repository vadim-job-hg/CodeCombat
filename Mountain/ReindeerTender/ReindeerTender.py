# http://codecombat.com/play/level/reindeer-tender
# This array contains the positions of the pens that we want to put the reindeer in.
penPositions = [{"x": 20, "y": 24}, {"x": 28, "y": 24}, {"x": 36, "y": 24}, {"x": 44, "y": 24}, {"x": 52, "y": 24}]
# This array is used to track which reindeer have been asssigned to which pen.
assignments = [None, None, None, None, None, ]
# And this array contains our reindeer.
friends = hero.findFriends()

# Figure out which reindeer are already in their pens.
for deerIndex in range(len(friends)):
    reindeer = friends[deerIndex]

    # Go through each position and see if it matches the reindeer's position.
    for posIndex in range(len(penPositions)):
        penPos = penPositions[posIndex]

        if penPos.x == reindeer.pos.x and penPos.y == reindeer.pos.y:
            # Put the reindeer in the assignments array in slot posIndex.
            assignments[posIndex] = penPositions[posIndex]
            # Remove the reindeer from the friends array.
            friends[deerIndex] = None
            # break out of the inner loop here to avoid confusion.
            break
            pass

# Assign the remaining reindeer to new positions.
for deerIndex in range(len(friends)):
    # If the reindeer in this array slot is null, skip this and continue to the next one.
    if not friends[deerIndex]:
        continue
    reindeer = friends[deerIndex]
    # Look for the first pen with nothing already assigned to it.
    for posIndex in range(len(penPositions)):
        # If there's nothing in this slot of the assignments array, then the pen is open.
        if not assignments[posIndex]:
            # Put the reindeer in the assignments array.
            assignments[posIndex] = friends[deerIndex]
            # Command the reindeer to move to the pen position.
            hero.command(assignments[posIndex], 'move', penPositions[posIndex])
            # break out of the inner for loop here so we don't reassign the deer.
            break
            pass
