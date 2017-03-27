# https://codecombat.com/play/level/phd-kitty
# Kitty is the smartest cougar. It knows everything.
# Let's make a show for those peasants.

# This function makes the pet say something like: "Miao"
def sayTwoWords(event):
    # Make the pet say the correct answer to the questions.
    pet.say('2')
    pass

# Use 'sayTwoWords' for the pet's "hear" event.
pet.on('hear', sayTwoWords)
# Now relax and watch the show.
hero.say("One plus one is...?")
hero.say("x^3 - 6x^2 + 12x - 8 = 0. What is x...?")
hero.say("How many moons does Mars have...?")
