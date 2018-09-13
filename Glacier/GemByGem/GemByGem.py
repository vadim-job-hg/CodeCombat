# Connect gems to a linked list to open the door.

# Use that gems a base for the list.
baseGem = hero.findByType("root-gem")[0]
# Those gems are not linked yet.
freeGems = hero.findByType("gem")

# Use the property "next" to link elements to the list.
# Append an element before the base gem.
freeGems[0].next = baseGem
# And one more at the new head of the list:
freeGems[1].next = freeGems[0]
# Next add more gems at the end.
baseGem.next = freeGems[2]
# Add two more gems one by one:
freeGems[2].next = freeGems[3]
freeGems[3].next = freeGems[4]
while True:
    if hero.isPathClear(hero.pos, {"x": 76, "y": 34}):
        hero.moveXY(76, 34)
