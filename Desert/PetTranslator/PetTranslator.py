# https://codecombat.com/play/level/pet-translator
# Those artillerymen don't understand you.
# Your pet should translate commands.

# This is an event handler for the pet's "hear" event.
def translate(event):
    # Get the heard message.
    message = event.message
    # If the message is "North":
    if message == "North":
        # The pet says "Htron".
        pet.say("Htron")
    # If the message is "South":
    if message == "South":
        # The pet says "Htuos".
        pet.say("Htuos")
        pass
    # If the message is "East":
    if message == "East":
        # The pet says "Tsae".
        pet.say("Tsae")


# Assign the event handler.
pet.on("hear", translate)

while True:
    enemy = hero.findNearestEnemy()
    # Don't attack Brawlers.
    if enemy and enemy.type != "brawler":
        hero.attack(enemy)
        # else:
        #    hero.moveXY(33, 25)

