# https://codecombat.com/play/level/soldier-ogre-and-peasant
# Deliver that trinity to the left side of the river.

# The soldier hates the ogre.
soldier = pet.findNearestByType("soldier")
# The ogre plans something bad against the peasant.
ogre = pet.findNearestByType("munchkin")
# Just a peasant.
peasant = pet.findNearestByType("peasant")
left = {'x':32,'y':38}
right = {'x':53,'y':41}
# Use pet.carryUnit(unit, x, y) to deliver units.
pet.carryUnit(ogre, left.x, left.y)
pet.carryUnit(soldier, left.x, left.y)
pet.carryUnit(ogre, right.x, right.y)
pet.carryUnit(peasant, left.x, left.y)
pet.carryUnit(ogre, left.x, left.y)
