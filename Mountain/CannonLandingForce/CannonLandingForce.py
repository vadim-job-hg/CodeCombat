# https://codecombat.com/play/level/cannon-landing-force
# We should send some soldiers to defend the mountain village.
# Also we need clear out old fire traps.
# For both of those goals we'll use the artillery!
# The artillery can launch soldiers and anti-trap shells over the mountains.

# The scout prepared a map of the landing zone.
# The map is 2 dimensional array, where cells are strings.
landingMap = hero.findNearest(hero.findFriends()).landingMap

# The cannons need to know the row, the column, and what's there.
# To get the element in row i and column j, use 'array[i][j]'.
# First, let's look at row 0 and column 0.
cell = landingMap[0][0]
# Next, say the coordinates and what's there.
hero.say("row 0 column 0 " + cell)

# Next cell is the 3rd row and the 2nd column.
hero.say("row 3 column 2 " + landingMap[3][2])

# Now do it yourself for the next point:
# The 2nd row and 1st column.
hero.say("row 2 column 1 " + landingMap[2][1])
# The 1st row and 0th column.
hero.say("row 1 column 0 " + landingMap[1][0])
# The 0th row and 2nd column.
hero.say("row 0 column 2 " + landingMap[0][2])
# The 1st row and 3rd column.
hero.say("row 1 column 3 " + landingMap[1][3])
