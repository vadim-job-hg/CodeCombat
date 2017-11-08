# https://codecombat.com/play/level/pet-quiz
# Let's ask your pet a little.

# Write an event handler function "petSay".
# The pet should say something in this function.

def petSay(event):
    pet.say('Yes')
pet.on("hear", petSay)

hero.say("Do you understand me?")
hero.say("Are you a cougar?")
hero.say("How old are you?")
# Ask two more questions.
hero.say("How old are you?")
hero.say("How old are you?")

