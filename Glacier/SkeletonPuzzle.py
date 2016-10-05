#https://codecombat.com/play/level/skeleton-puzzle
# Solve the puzzle and the treasures will be yours.
# Say numbers from 1 to 8 to move skeletons.

# The necromancer always knows the puzzle state.
boneMaster = hero.findFriends()[0]
puzzleState = boneMaster.getPuzzleState()
# The result state should be this:
goalState = [[1,2,3],[4,5,6],[7,8,0]]

# Solve, Solve, Solve!
for number in [2, 3, 6, 2, 3, 5, 6, 5, 8]:
    hero.say(number)
