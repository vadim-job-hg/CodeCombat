# https://codecombat.com/play/level/three-step-password

# Find a password for the gates and defeat ogres.

# Get the secret message.
hero.moveXY(52, 50)
friend = hero.findNearest(hero.findFriends())
message = friend.message

# Get the separator symbol.
hero.moveXY(66, 34)
friend = hero.findNearest(hero.findFriends())
separator = friend.separator

# Get the index.
hero.moveXY(52, 18)
friend = hero.findNearest(hero.findFriends())
index = friend.index;

# Move to the gates.
hero.moveXY(44, 34)
# Split the message with the separator to get an array.
messages = message.split(separator)
# Get the password from the array of words by the index.
password = messages[index]
# Say the password.
hero.say(password)

# Defeat the ogres.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

