# https://codecombat.com/play/level/anonymous-bank

# Find passwords and get treasures.

# We intercepted a scout with passwords and some words.
message = hero.findNearest(hero.findFriends()).message
# Here we will store passwords.
passwords = []
# All passwords have 5 letters.All real passwords have 5 letters.
passwordLength = 5

# Split the message by ";" and save words in a variable.
words = message.split(";")
# Iterate over all words.
for word in words:
    # Trim each word to remove whitespace.
    wordt = word.trim()
    # If the length of the cleaned word is 5:
    if len(wordt)==5:
        # Add the cleaned word to the passwords array:
        passwords.push(wordt)


# Move to the marks and say passwords:
marksPos = [{"x": 12, "y": 14}, {"x": 38, "y": 38},
            {"x": 42, "y": 16}, {"x": 54, "y": 12}];
for i in range(4):
    pos = marksPos[i]
    hero.moveXY(pos.x, pos.y)
    password = passwords[i]
    if password:
        hero.say(password)
    else:
        hero.say("qwerty")
