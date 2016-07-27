# http://codecombat.com/play/level/the-spy-among-us
# The inner gate can hold against ogres for a long time.
# But one of these peasants is an OGRE SPY!
# We have a hint: the spy's name contains the letter "z"

# This function checks if an array contains a certain number:
def numberInArray(array, number):
    for i in range(len(array)):
        if array[i] == numb:
            return True
    return False


# This function should check if a string contains a certain character:
def letterInWord(word, letter):
    # Iterate over every index of the string and check if the character matches the letter:
    for x in range(0, len(word), 1):
        item = word.substr(x, 1)
        if item == letter:
            return True
    return False


mineDistance = 5

spyLetter = "z"
friends = hero.findFriends()

for j in range(len(friends)):
    friendName = friends[j].id
    if letterInWord(friendName, spyLetter):
        # Reveal the spy!
        hero.say(friendName + " is a spy!")
    else:
        hero.say(friendName + " is a friend.")  # ∆ Remove this line after writing the letterInWord function.
