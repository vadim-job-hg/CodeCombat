# https://codecombat.com/play/level/perimeter-defense
# We need to build guard towers around the village.
# Each peasant can build one tower.
# Show them the place to build.
# These towers are automatic and will attack ALL units outside the town.

# First move along the north border (y=60) from x=40 to x=80 with the step 20.
# `range` doesn't include the second edge.
for x in range(40, 81, 20):
    # Move at each point and say anything.
    hero.moveXY(x, 60)
    hero.say("Here")
# Next move along the east border (x=80) from y=40 to y=20 with the negative step -20.
for y in range(40, 19, -20):
    hero.moveXY(80, y)
    hero.say("Here")
# Continue for the two remaining borders.
# Next the south border (y=20) from x=60 to x=20 with the negative step -20.
for x in range(60, 19, -20):
    hero.moveXY(x, 20)
    hero.say("Here")
# Next the west border (x=20) from y=40 to y=60 with the step 20.
for y in range(40, 61, 20):
    hero.moveXY(20, y)
    hero.say("Here")

# Don't forget hide inside the village.
hero.moveXY(50, 40)
