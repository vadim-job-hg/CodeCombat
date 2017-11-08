# https://codecombat.com/play/level/flawless-pairs
# Collect 4 pairs of gems.
# Each pair must contain equal valued gems.
# Return to the start point to get hasted.

# This function returns two items with the same value.
def findValuePair(items):
    # Check each possible pair in the array.
    # Iterate indexes 'i' from 0 to the second to last one.
    for i in range(len(items) - 1):
        # Iterate indexes 'j' from 'i+1' to the last.
        for j in range(i + 1, len(items)):
            # If we found a pair with two equal gems, then return them.
            if items[i].value == items[j].value:
                return [items[i], items[j]]
    # Return an empty array if no pair exists.
    return None


while True:
    gems = hero.findItems()
    gemPair = findValuePair(gems)
    # If the gemPair exists, collect the gems!
    if gemPair:
        # Move to the first gem first (gemPair[0]).
        hero.moveXY(gemPair[0].pos.x, gemPair[0].pos.y)
        # Return to get the haste from the wizard.
        hero.moveXY(40, 44)
        # Move to the second gem first (gempPair[1]).
        hero.moveXY(gemPair[1].pos.x, gemPair[1].pos.y)
        # Return to get the haste from the wizard.
        hero.moveXY(40, 44)
