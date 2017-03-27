# https://codecombat.com/play/level/trojan-yeti

# You need to defeat ogres.
# Send wereyeti peasants to the ogre camp and watch.

# This function returns a friendly unit by the name.
def findFriendByName(name):
    friends = hero.findFriends()
    for i in range(len(friends)):
        if friends[i].id == name:
            return friends[i]
    return None

# The sergeant wrote the list of wereyeti peasants' names.
sergeant = hero.findNearest(hero.findFriends())
wereList = sergeant.wereList
# The list isn't clean and contains redundant spaces.
wereNames = wereList.split(",")

# Iterate through wereNames array:
for name in wereNames:
    # Trim the whitespace from the name
    # and save it in the new variable:
    trimed = name.trim()
    # Use findFriendByName function to find a wereyeti:
    wereyeti = findFriendByName(trimed)
    # Command that unit move to the ogre camp:
    hero.command(wereyeti, 'move', {'x':48, 'y':48})
