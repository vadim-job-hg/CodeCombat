# https://codecombat.com/play/level/northwest
# Your pet should find and bring a potion to the hero.

# This function checks if the word is in the text.
def wordInText(text, word):
    # Iterate letter indexes in the text.
    for i in range(len(text) - len(word)):
        # For each index loop through the word.
        for j in range(len(word)):
            # Store a shifted index i + j.
            shiftedIndex = i + j
            # If a text letter with the shifted index.
            # isn't equal a word letter with the index "j":
            if text[shiftedIndex] != word[j]:
                # Break the loop.
                break
            # If it was the last letter in the word:
            if shiftedIndex == len(text) - len(word) - 1:
                # Then the word is in the text.
                # Return True.
                return True

    # Nothing. Return False.
    return False


# Listen guides where to run.
def onHear(event):
    # If "west" in the phrase, pet should run left.
    if wordInText(event.message, "west"):
        pet.moveXY(pet.pos.x - 28, pet.pos.y)
    # If "north" in the phrase, pet should run up.
    elif wordInText(event.message, "north"):
        pet.moveXY(pet.pos.x, pet.pos.y + 24)
    # Else the pet should try to fetch a potion.
    else:
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)


pet.on("hear", onHear)
