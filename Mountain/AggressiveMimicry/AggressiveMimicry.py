# https://codecombat.com/play/level/aggressive-mimicry
# Protect the village from ogres.
# Watch for ogres, peasants and "peasants".

# This function checks if the text starts with the word.
def startsWith(text, word):
    # If the word is longer then the text:
    if len(word) > len(text):
        return False
    # Loop indexes for the word.
    for index in range(len(word)):
        # If letters with the same index are different:
        if word[index] != text[index]:
            # Then the word doesn't coincide with the text.
            return False
    # We checked all letters and they are the same.
    return True


ogreNameStart = "Zog"

while True:
    enemy = hero.findNearestEnemy()
    suspect = hero.findNearest(hero.findFriends())
    # Use the function "startsWith" to check
    # if suspect's name (id) starts with "Zog", attack:
    if startsWith(suspect.id, ogreNameStart):
        # Else if an enemy here, then attack it:
        hero.attack(suspect)
    elif enemy:
        hero.attack(enemy)
    # Else return to the mark:
    else:
        hero.moveXY(27, 27)

