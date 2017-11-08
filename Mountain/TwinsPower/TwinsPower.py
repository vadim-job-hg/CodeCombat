# https://codecombat.com/play/level/twins-power
# We have lured the huge ogre in the temple of the Moon and the Sun.
# There are four pairs of twins, they should pray by pairs.
# You need to find twins and call them.

# Twins have almost the same names, only the last letter is different.
# This function checks if the pair of units are twins.
def areTwins(unit1, unit2):
    name1 = unit1.id
    name2 = unit2.id
    if name1.length != name2.length:
        return False
    for i in range(name1.length - 1):
        if name1[i] != name2[i]:
            return False
    return True


# Iterate over all pairs of paladins and say() their name by pairs if they are twins.
for paladin1 in hero.findFriends():
    for paladin2 in hero.findFriends():
        if (paladin1.id != paladin2.id and areTwins(paladin1, paladin2)):
            hero.say(paladin1.id + " " + paladin2.id)
# For example: hero.say("NameTwin1 NameTwin2")

# When twins are in their spots, lure the ogre.
# Don't be afraid of beams - they are dangerous only for ogres.
hero.wait(5)
hero.moveXY(63, 38)
hero.moveXY(16, 38)
