# http://codecombat.com/play/level/in-my-name
# You must to find the treasure.
# Use Thoktar's name as a hint.
# The correct treasure chest is the same number as the index of 'z' in Thoktar's name.


# This function should return the number where letter is in word:
def letterIndex(word, letter):
    # Step through each letter as an index of the given word
    for index in range(0, len(word), 1):
        # Compare the letter in the word with the given letter
        if (word[index] == letter):
            # If it's required letter then return the current index
            return index
    # If nothing, return a default value
    return 0


ogreLetter = "z"
shaman = hero.findByType("thoktar")[0]

# Find the index and use it for finding the treasure.
chestIndex = letterIndex(shaman.id, "z")
hero.moveXY(16 + chestIndex * 8, 36)
