# https://codecombat.com/play/level/scylla-and-charybdis
# Listen mages' phrases and hide.

# The event handler for the pet.
def hearAndDodge(event):
    # Find a sorcerer and a warlock.
    sorcerer = pet.findNearestByType("sorcerer")
    warlock = pet.findNearestByType("warlock")
    # If the sorcerer says something:
    if event.speaker == sorcerer:
        # If the phrase is "Fire":
        if event.message == "Fire":
            # Hide to the left mark.
            pet.moveXY(26, 46)
        # If the phrase is "Burn":
        if event.message == "Burn":
            # Hide near the angel statue (the top mark).
            pet.moveXY(42, 59)
    # If the warlock says something:
    if event.speaker == warlock:
        # If the phrase is "Fire":
        if event.message == "Fire":
            # Hide to the right mark.
            pet.moveXY(53, 34)
        # If the phrase is "Burn":
        if event.message == "Burn":
            pet.moveXY(34, 26)
            # Hide near the viper pillar (the bottom mark).


pet.on("hear", hearAndDodge)
