# https://codecombat.com/play/level/olympic-race
# The pet must win the race.
# Runners should touch a mark and run back.

def waitAndRun(event):
    referee = pet.findNearestByType("wizard")
    # If the speaker is referee and the message is "Start":
    if event.speaker==referee and event.message == 'Start':
        # Make the pet run to the red mark.
        pet.moveXY(54, 27)
        # Then run back.
        pet.moveXY(6, 28)

# Assign the waitAndRun function to handle "hear" events.

pet.on("hear", waitAndRun)
