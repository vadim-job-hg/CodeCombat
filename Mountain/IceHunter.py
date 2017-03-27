# https://codecombat.com/play/level/ice-hunter
# Hunt for 4 yaks. Choose only the small ones.
# Small yak names contain a "bos" substring.

# This function checks if a word contains a substring.
def isSubstring(word, substring):
    # We iterate through the start indexes only.
    rightEdge = len(word) - len(substring)
    # Loop through the indexes of the word.
    for i in range(rightEdge + 1):
        # For each of them loop through the substring
        for j in range(len(substring)):
            # Use an offset for the word's indexes.
            shiftedIndex = i + j
            # If letters aren't the same:
            if word[shiftedIndex] != substring[j]:
                # Check the next start index in the word.
                break
            # If it was the last letter in the substring:
            if j == len(substring) - 1:
                # Then the substring is in the word.
                return True
    # We haven't found the substring in the word.
    return False

# Loop through all enemies.
enemies = hero.findEnemies()
for e  in range(len(enemies)):
    enemy = enemies[e]
    # Use the function isSubstring to check
    # if an enemy name (id) contains "bos":
    if(isSubstring(enemy.id, 'bos')):
        # Then defeat it.
        while enemy.health>0:
            hero.attack(enemy)
