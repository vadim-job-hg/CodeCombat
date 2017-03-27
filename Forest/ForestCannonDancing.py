# https://codecombat.com/play/level/forest-cannon-dancing
# Your pet should run back and forth on the marks.
# The hero should cheer the whole time!

# Write the event function "runBetween" for the pet.
# This function should make the wolf run back and forth:
# First, the pet should run to the right mark, then the left one:
def runBetween(event):
    while True:
        pet.moveXY(48,8)
        pet.moveXY(12,8)

pet.on("spawn", runBetween)
# Cheer up your pet. Don't remove this:
while True:
    hero.say("Run!!!")
    hero.say("Faster!")
