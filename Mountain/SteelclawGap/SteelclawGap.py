# This level introduces the % operator, also known as the modulo operator.
# a % b returns the remainder of a divided by b
# This can be used to wrap around to the beginning of an array when an index might be greater than the length


defendPoints = [{"x": 35, "y": 63}, {"x": 61, "y": 63}, {"x": 32, "y": 26}, {"x": 64, "y": 26}]

summonTypes = ["soldier", "soldier", "soldier", "soldier", "archer", "archer", "archer", "archer"]


# You start with 360 gold to build a mixture of soldiers and archers.
# hero.built is an array of the troops you have built, alive or dead
# Here we use "len(hero.built) % len(summonTypes)" to wrap around the summonTypes array

def summonTroops():
    type = summonTypes[len(hero.built) % len(summonTypes)]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)


def commandTroops():
    friends = hero.findFriends()
    for friendIndex, friend in enumerate(friends):
        # Use % to wrap around defendPoints based on friendIndex
        hero.command(friend, 'defend', defendPoints[friendIndex % len(defendPoints)])
        pass
        # Command your minion to defend the defendPoint


while True:
    summonTroops()
    commandTroops()
