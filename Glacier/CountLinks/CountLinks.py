# https://codecombat.com/play/level/count-links
# Each cannon has from 1 to 5 shells and shoot them once.
# The first (index 0) has 1, the second - 2 and etc.

# The function find the element by index in a linked list.
def elementByIndex(linkedList, index):
    current = linkedList
    # Iterate from 0 to "index" (exclusive):
    for i in range(index):
        # Each element should have a property "next".
        # Reassign "current" with the next element:
        current = current.next
        # If the current element is empty, stop it:
        if not(current):
            break
    # Return the current element.
    return current

# The reference to the linked list of cannons.
cannonList = hero.findNearest(hero.findFriends())

while True:
    enemies = hero.findEnemies()
    if len(enemies) > 0:
        # We need a cannon with the certain number.
        hero.say(elementByIndex(cannonList, len(enemies) - 1))
