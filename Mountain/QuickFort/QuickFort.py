# https://codecombat.com/play/level/quick-fort
# We should quickly build a fort!
# Each peasant has one speciality and can build only one type of constructions.
# Carpenter - fences; Mason - towers; builder - tents.
# The foreman mixed their names in one list, but in the specific order.
# The list looks like [builder, mason, carpenter, builder, mason, carpenter, ...]
# Use that list and assign the proper task for each peasant.

# The foreman stored the list of workers' names as a property.
foreman = hero.findNearest(hero.findFriends())
workerNameList = foreman.workerList

# Use loops with steps to choose each third element.
# First, you need assign workers for the towers.
# Use start value 1 and increase the index by 3.
for i in range(1, len(workerNameList), 3):
    # For each of them say the name and what to build.
    hero.say(workerNameList[i] + " - tower")

# First, you need assign workers for the tents.
# Use start value 0 and increase the index by 3.
for i in range(0, len(workerNameList), 3):
    # For each of them say to build "tent".
    hero.say(workerNameList[i] + " - tent")

# Finally, you need assign workers for the fence.
# Use start value 2 and increase the index by 3.
for i in range(2, len(workerNameList), 3):
    hero.say(workerNameList[i] + " - fence")
    # For each of them say to build "fence".For each of them say to build "fence".


# Now watch for the battle or help your army.
