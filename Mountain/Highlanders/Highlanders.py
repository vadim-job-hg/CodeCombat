# http://codecombat.com/play/level/highlanders
# You must defeat the ogres
# But they are using black magic!
# Only the highlander soldiers are immune.
# Find highlanders, their names always contain "mac"

highlanderName = "mac"


# This function should search for a string inside of a word:
def wordInString(string, word):
    lenString = len(string)
    lenWord = len(word)
    # Step through indexes (i) from 0 to (lenString - lenWord)
    for index in range(0, (lenString - lenWord), 1):
        world = string.substr(index, lenWord)
        if (world == highlanderName):
            return True
            # For each of them through indexes (j) of the word length

            # If [i + j]th letter of the string is not equal [j]th letter of world, then break loop

            # if [j]th is the last letter of the word (j == lenWord - 1), then return True.

    # If loops are ended then the word is not inside the string. Return False.

    return False  # ∆ Remove this when the function is written.


# Look at your soldiers and choose highlanders only
soldiers = hero.findFriends()
for soldier in soldiers:
    if wordInString(soldier.id, highlanderName):
        hero.say(soldier.id + " be ready.")

#
hero.say("ATTACK!!!")
