# https://codecombat.com/play/level/sand-mushrooms
# Collect 9 mushrooms.

# This function make the pet fetch potions for you.
def onSpawn(event):
    while True:
        # Pets can find the nearest item by its type.
        potion = pet.findNearestByType("potion")
        # Make the pet fetch the potion if it exists:
        if potion:
            pet.fetch(potion)

pet.on("spawn", onSpawn)

# Mushrooms are burning, don't hurry to collect them.
while True:
    someItem = hero.findNearestItem()
    if someItem and hero.health > hero.maxHealth / 3:
        # Collect the someItem:
        hero.move(someItem.pos)
        pass
