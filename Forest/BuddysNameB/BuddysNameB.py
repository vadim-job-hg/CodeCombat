# https://codecombat.com/play/level/buddys-name-b
# The pet should greet the hero and the peasant.

# Use this function as a handler for "hear" events on pet.
def sayHello(event):
    # Make the pet say "Hello".
    pet.say('Hello')
    pass

# Use the pet.on(eventType, eventHandler) method
# Assign the sayHello function to handle "hear" events.
pet.on('hear', sayHello)

# It must be after "pet.on".
hero.say("Hello, Kitty!")
