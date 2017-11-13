# https://codecombat.com/play/level/explosive-sorting

# Sort the bombs by their health to clear the passage.

# The function swaps elements and bombs in the array.
def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
    # Voice control!
    hero.say(index1 + " and " + index2)

# The function sorts units by their health.
def selectionSort(units):
    # Iterate start indexes from 0th to the prev last.
    for i in range(len(units) - 1):
        minIndex = i;
        # Iterate indexes from (minIndex + 1) to the last:
        for j in range(minIndex + 1, len(units)):
            # If the unit with current index has lower
            # health than the unit with minIndex:
            if units[j].health<units[minIndex].health:
                # Then update minIndex to the current one:
                minIndex = j;
        if minIndex != i:
            swap(units, i, minIndex)

bombArray = hero.findFriends()[0].bombArray
selectionSort(bombArray)
