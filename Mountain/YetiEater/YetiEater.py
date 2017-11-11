# https://codecombat.com/play/level/yeti-eater
# Yetis surround us and we need to kill them.
# Luckily the wizard had time to cast the sleep spell.
# Your hero can devour the yetis' vital powers when they are killed.
# Kill them in the order from weakest to the strongest.

# The wizard sorted enemies, but in the order from the strongest to the weakest.
wizard = hero.findNearest(hero.findFriends())
yetis = wizard.findEnemies()
# You need iterate the yetis list in the reverse order with a 'for-loop'.
# The start value should be 'len(yetis) - 1'.
# Iterate while the index greater than -1.
# Use the negative step -1.
index = len(yetis)-1
while index>=0:
    # Attack each enemy while its health greater than 0.
    while yetis[index].health>0:
        hero.attack(yetis[index])
    index = index - 1

# Look at the guide to get hints.
