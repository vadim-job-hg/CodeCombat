# https://codecombat.com/play/level/dangerous-key
# Listen to the paladin and fetch the right key.

def onHear(event):
    # The pet can find the paladin and keys.
    paladin = pet.findNearestByType("paladin")
    goldKey = pet.findNearestByType("gold-key")
    silverKey = pet.findNearestByType("silver-key")
    bronzeKey = pet.findNearestByType("bronze-key")
    # If event.speaker is the paladin:
    if event.speaker == paladin:
        # If event.message is "Gold":
        if event.message == "Gold":
            # The pet should fetch the gold key.
            pet.fetch(goldKey)
        # If event.message is "Silver":
        if event.message == "Silver":
            # The pet should fetch the silver key.
            pet.fetch(silverKey)
        # If event.message is "Bronze":
        if event.message == "Bronze":
            # The pet should fetch the bronze key.
            pet.fetch(bronzeKey)

pet.on("hear", onHear)
