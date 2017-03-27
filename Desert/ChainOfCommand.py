# https://codecombat.com/play/level/chain-of-command
# Only your pet can wake the wizard up.

# It's an event handler for pet's "hear".
def barkForMaster(event):
    # "event.speaker" exists only for "hear" events.
    # Check if the pet has heard the hero:
    if event.speaker == hero:
        pet.say("WOOF")

# Assign the event handler for "hear" event.
pet.on("hear", barkForMaster)

while True:
    enemies = hero.findEnemies()
    # Check if there are any enemies in enemies array:
    if(len(enemies)>0):
        # Alarm the pet with "say".
        hero.say('WOOF')
        # Move into the camp
        if(hero.isReady('jump')):
            hero.jumpTo({'x':30, 'y':33})
        else:
            hero.moveXY(30, 33)
        # Then return to the look-out point.
        hero.moveXY(30, 15)
