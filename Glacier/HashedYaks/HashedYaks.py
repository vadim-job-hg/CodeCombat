# https://codecombat.com/play/level/hashed-yaks
# Find cell numbers with awake yaks.

# The farmer know which yaks aren't sleeping.
farmer = hero.findFriends()[0]
yakNameList = farmer.yakList

# This hash function convert names into a number.
def hashName(name):
    hero.say(name)
    asciiCode = ord(name[0])
    return (asciiCode - 65) % 12

# Iterate the list of yak names (yakList):
for yak in yakNameList:
    # Use the hash function for each name and
    # say the result number.
    hero.say(hashName(yak))
