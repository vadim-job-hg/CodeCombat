# https://codecombat.com/play/level/gem-by-gem
# Connect gems to a linked list to open the door.

# Use that gems a base for the list.
baseGem = hero.findByType("root-gem")[0]
# Those gems are not linked yet.
freeGems = hero.findByType("gem")

# Use the property "next" to link elements to the list.
# Append an element before the base gem.
freeGems[0].next = baseGem
# And one more at the new head of the list:

# Next add more gems at the end.
baseGem.next = freeGems[2]
# Add two more gems one by one:


while True:
    if hero.isPathClear(hero.pos, {"x": 76, "y": 34}):
        hero.moveXY(76, 34)
