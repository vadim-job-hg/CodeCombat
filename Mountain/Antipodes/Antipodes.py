# https://codecombat.com/play/level/antipodes
# The warlock used the "clone" spell and created evil antipodes of our archers.
# But even that evil spell has weakness.
# If your archer touches his antipode, then it will disappear.
# If an archer touches the wrong clone or attacks one of them, then the clones start to fight.
# We can find antipodes by their names - they are each other's reverse.

# This function check two units whether they are antipodes or not.
def areAntipodes(unit1, unit2):
    reversed1 = ""
    for i in range(len(unit1.id) - 1, -1, -1):
        reversed1 += unit1.id[i]
    return reversed1 == unit2.id


friends = hero.findFriends()
enemies = hero.findEnemies()

# Find antipodes for each of your archers.
# Iterate all friends.
for friend in friends:
    # For each of friends iterate all enemies.
    for enemy in enemies:
        # Check if the pair of the current friend and the enemy are antipodes.
        if areAntipodes(friend, enemy):
            # If they are antipodes, command the friend move to the enemy.
            hero.command(friend, 'move', enemy.pos)

# When all clones disappears, attack the warlock.
hero.wait(20)
enemies = hero.findEnemies()
while len(enemies) == 1:
    hero.attack(hero.findNearestEnemy())
