# https://codecombat.com/play/level/buddys-name
# We need to know the name of our new pet.

# This function is using as a callback for a pet.
def sayName(event):
    pet.say("Meow Purr Meow")
    pet.say("Purr Purr")
    pet.say("Meow")
    pet.say("Meow")
    pet.say("Meow Purr Meow Meow")

# Use "pet.on" method to assign "sayName" function as the event handler for "hear".
pet.on("hear", sayName)
hero.say("What's you name, buddy?")
hero.say("Could you repeat it?")
