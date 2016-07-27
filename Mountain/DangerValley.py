# http://codecombat.com/play/level/danger-valley
# Ogres have taken some peasants hostage!
# Your scouts have given you the intel required to lay an ambush.
# this.grid holds an array of arrays.
# Inside these sub-arrays, 0 is a peasant and 1 is an ogre!
# Use this information to setup fire-traps to defeat the convoy.

# First, remember the containing array is just an array!
# Iterate over all the elements of this array.
for i in range(len(self.grid)):
    row = self.grid[i]
    for j in range(len(row)):
        if (row[j] == 1):
            self.buildXY('fire-trap', 36 + j * 5, 20 + i * 6)
            # Now, row is just another array!
            # Iterate over all the tiles in this array:

            # Build a fire-trap if the tile is 1.

# Finally, retreat back to cover.
self.moveXY(20, 42)
self.moveXY(29, 66)
