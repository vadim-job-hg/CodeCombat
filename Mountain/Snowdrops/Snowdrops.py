# https://codecombat.com/play/level/snowdrops
# We need to clear the forest of traps using the cannon!
# The scout prepared a map of the forest.
# But the map has rows with different lengths, so be sure before you shoot.

# Get the map of the forest.
forestMap = hero.findNearest(hero.findFriends()).forestMap

# The map is an array of arrays, where 1 is clear and 0 is a trap.
# The first sure shot.
hero.say("Row " + 0 + " Column " + 1 + " Fire!")

# But for the next points we are not sure and should check before shooting.
# There are an array of points to check.
cells = [{"row": 0, "col": 4}, {"row": 1, "col": 0}, {"row": 1, "col": 2}, {"row": 1, "col": 4},
         {"row": 2, "col": 1}, {"row": 2, "col": 3}, {"row": 2, "col": 5}, {"row": 3, "col": 0},
         {"row": 3, "col": 2}, {"row": 3, "col": 4}, {"row": 4, "col": 1}, {"row": 4, "col": 2},
         {"row": 4, "col": 3}, {"row": 5, "col": 0}, {"row": 5, "col": 3}, {"row": 5, "col": 5},
         {"row": 6, "col": 1}, {"row": 6, "col": 3}, {"row": 6, "col": 4}, {"row": 7, "col": 0}];

for cell in cells:
    row = cell["row"]
    col = cell["col"]
    # First check if row is less than the length of forestMap.
    if row < len(forestMap):
        # Next, check if col is less than the length of forestMap[row].
        if col < len(forestMap[row]):
            # Now we sure that the cell exists and can check its value.
            # If it's 0 (zero), then say where to shoot.
            if forestMap[row][col] == 0:
                hero.say("Row " + row + " Column " + col + " Fire!")
