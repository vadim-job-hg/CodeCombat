# https://codecombat.com/play/level/long-road
# Move to the right side of the forest.

# This function should check for items near the pet and fetch them.
def fetchPotions(event):
    # Complete this function:
    # Don't forget to use a "while-true loop":
    while True:
        item = pet.findNearestItem()
        if item:
            pet.fetch(item)
    pass

# Assign the function 'fetchPotions' for the pet event "spawn".
pet.on("spawn", fetchPotions)
hero.moveXY(78, 35);

