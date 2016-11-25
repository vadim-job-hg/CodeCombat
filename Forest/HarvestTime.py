# This line will get the peasant to the first mushroom.
hero.moveXY(hero.xmin, hero.ymin)

# Mushrooms have x-coordinates between xmin and xmax,
# and y-coordinates between ymin and ymax.
# Try using loops to harvest all of the mushrooms
# without typing very many lines of code.
# It can be done in less than 5 lines!
for y in range(hero.ymin, hero.ymax + 1, 10):
    for x in range(hero.xmin, hero.xmax + 1, 10):
        hero.moveXY(x, y)
# Try to have the hero.moveXY() function show up
# as few times as possible in your code.
