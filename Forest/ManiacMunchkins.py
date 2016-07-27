# https://codecombat.com/play/level/maniac-munchkins
# Another chest in the field for the hero to break open!
# Attack the chest to break it open.
# Some munchkins won't stand idly by while you attack it!
# Defend yourself when a munchkin gets too close.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady('cleave'):
        # First priority is to cleave if it's ready:
        hero.cleave(enemy)
        pass
    elif distance < 5:
        # Attack the nearest munchkin that gets too close:
        hero.attack(enemy)
        pass
    else:
        # Otherwise, try to break open the chest:
        hero.attack('Chest')
        pass
