# This line will get the peasant to the first mushroom.
self.moveXY(self.xmin, self.ymin)

# Mushrooms have x-coordinates between xmin and xmax,
# and y-coordinates between ymin and ymax.
# Try using loops to harvest all of the mushrooms
# without typing very many lines of code.
# It can be done in less than 5 lines!
for y in range(self.ymin, self.ymax + 1, 10):
    for x in range(self.xmin, self.xmax + 1, 10):
        self.moveXY(x, y)
# Try to have the self.moveXY() function show up 
# as few times as possible in your code.
