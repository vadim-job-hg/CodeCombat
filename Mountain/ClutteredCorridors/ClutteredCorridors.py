# https://codecombat.com/play/level/cluttered-corridors

# Help the pet find the exit.

def onHear(event):
    word = event.message
    # Convert the word to lower case.
    word = word.toLowerCase()
    if word == "north":
        pet.moveXY(pet.pos.x, pet.pos.y + 16)
    elif word == "east":
        pet.moveXY(pet.pos.x + 12, pet.pos.y)
    elif word == "south":
        pet.moveXY(pet.pos.x, pet.pos.y - 16)
    elif word == "west":
        pet.moveXY(pet.pos.x - 12, pet.pos.y)

# Assign the event handler for the pet's "hear" event.
pet.on('hear', onHear)
