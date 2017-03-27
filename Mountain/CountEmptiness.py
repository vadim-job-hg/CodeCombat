# https://codecombat.com/play/level/count-emptiness
# Solve the riddler puzzle and find the treasure.
# Count whitespaces in on both sides of a riddle.

# This function moves the hero N steps right.
def moveNSteps(n):
    hero.moveXY(hero.pos.x + 8 * n, hero.pos.y)

# Read the riddle.
riddle = hero.findNearestEnemy().riddle
# Trim whitespaces from both side and save it in a variable
trimmed = riddle.trim()
# Find the difference between the lengths
#
spot = len(riddle)-len(trimmed)
# Use this result and moveNSteps function to find the spot.
moveNSteps(spot)
# Say something there!
hero.say('something')
