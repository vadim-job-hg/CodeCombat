# http://codecombat.com/play/level/grid-search
# The treasure somewhere between trees.
# The coordinates are 'x: ?0, y: ?0'. 
# Move at all potential points and show to peasants where to dig.

leftBorder = 20
rightBorder = 61
bottomBorder = 20
topBorder = 51
step = 10

# Iterate X coordinates from the left to right border with step 10.
for x in range(leftBorder, rightBorder, step):
    # Use a nested loop to iterate through Y coordinates for each X.
    # Iterate y coordinates from the bottom to top border with step 10.
    for y in range(leftBorder, rightBorder, step):
        # Move to the point with coordinates X, Y and say anything.
        hero.moveXY(x, y)
        hero.say('Djigurda')

# Allow peasants to check the last point.
hero.moveXY(20, 10)
