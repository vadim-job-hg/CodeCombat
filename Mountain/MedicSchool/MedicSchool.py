# https://codecombat.com/play/level/medic-school
# This function checks if the phrase starts with the word.
def startsWith(phrase, word):
    # If the word is longer than the text, return False.
    if len(word) > len(phrase):
        return False
    # Loop through the indexes of word and text.
    for index in range(len(word)):
        # If characters with the same index are different:
        if word[index] != phrase[index]:
            # Return False.
            return False
    # We checked all letters and they are the same.
    # Return true.
    return True

def onHear(event):
    # Take potions only from experts.
    if startsWith(event.speaker.id, "Exp"):
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)
            pet.moveXY(28, 34)

pet.on("hear", onHear)
while True:
    mushrooms = hero.findByType("mushroom")
    nearest = hero.findNearest(mushrooms)
    if nearest and hero.health>700:
        hero.moveXY(nearest.pos.x, nearest.pos.y)
