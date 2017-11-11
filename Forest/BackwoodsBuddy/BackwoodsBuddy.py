# https://codecombat.com/play/level/backwoods-buddy
# You now have a pet!

def speak(event):
    pet.say("Hi")
    pass
    # Your pet should respond with pet.say()


# This tells your pet to run the speak() function when she hears something
pet.on("hear", speak)

# Talk to your pet!
hero.say("Hello Kitty")
