# https://codecombat.com/play/level/yeti-beater
# Follow by one of the peasants and escape from yetis.

def startsWith(phrase, word):
    if len(word) > len(phrase):
        return False
    # Iterate indexes from 0 to the length of the word.
    for index in range(0, len(word)):
        # If characters with the same index
        # in the word and in the phrase are not equal.
        if word[index]!=phrase[index]:
            # Then return False.
            return False
    # All letters in the word checked, then return true.
    return True

# Follow by a local guide whose name starts with "Mac".
guides = hero.findFriends()
for gIndex in range(len(guides)):
    guide = guides[gIndex]
    if startsWith(guide.id, "Mac"):
        while True:
            hero.move(guide.pos)
