# https://codecombat.com/play/level/buddys-name-a
# The peasant need to know the name of the pet.

# Use this function as a handler for "hear" events on pet.
def saySomething(event):
    # Make the pet say something.
    pet.say('something')
    pass

# Use the pet.on(eventType, eventHandler) method
# Assign the saySomething function to handle "hear" events.
pet.on('hear', saySomething)
