# https://codecombat.com/play/level/first-out
# Defeat incoming ogres and bring gems.
units = hero.findFriends()
# The sergeant can command by units.
sergeant = hero.findByType("paladin", units)[0]
# The scout will help to find enemies.
scout = hero.findByType("griffin-rider", units)[0]
soldiers = hero.findByType("soldier", units)
peasants = hero.findByType("peasant", units)

# First we need prepare soldiers. First we need prepare soldiers.
for soldier in soldiers:
    # The sergeant can command to enqueue an unit.
    sergeant.enqueue(soldier)
# Now prepare and "enqueu" peasants.
for peasant in peasants:
    # The sergeant can command to enqueue an unit.
    sergeant.enqueue(peasant)

while True:
    enemy = scout.findNearestEnemy()
    # When enemies are here.
    if enemy:
        for s in soldiers:
            # Send soldiers with the "dequeue" method.
            sergeant.dequeue()
        break

while True:
    enemy = scout.findNearestEnemy()
    # If enemies are dead.
    if not enemy:
        # "dequeue" the remaining peasants
        for s in peasants:
            sergeant.dequeue()
        break

