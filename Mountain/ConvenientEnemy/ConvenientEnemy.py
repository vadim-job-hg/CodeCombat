# https://codecombat.com/play/level/convenient-enemy
# Ogres are hiding in woods. Protect the peasants.
# The last word in the peasants' messages are a hint.

for x in range(8, 73, 16):
    hero.moveXY(x, 22)
    # Peasants know whom to summon.
    peasant = hero.findNearest(hero.findFriends())
    message = peasant.message
    if message:
        # Words are seaparated by whitespaces.
        words = message.split(" ")
        # "words" is an array of words from the "message".
        # Get the last word. It's the required type.
        last = words[len(words)-1]
        # Summon the required unit type.
        hero.summon(last)

for i in range(len(hero.built)):
    unit = hero.built[i]
    # Command the unit to defend the unit's position.
    hero.command(unit, 'defend', unit.pos)

# Defend the last point yourself:
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

