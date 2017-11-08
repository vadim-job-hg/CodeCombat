# https://codecombat.com/play/level/hot-gate
# Use voice commands to command the artillery.

while True:
    enemy = pet.findNearestEnemy()
    if not enemy:
        continue
    # Scouts are fast. We need stop them.
    if enemy.type == "scout":
        distance = pet.distanceTo(enemy)
        if pet.isReady("cold-blast") and  distance < 5:
            pet.coldBlast()
    else:
        # If the enemy on the left of the pet:
        if enemy.pos.x<pet.pos.x:
            # Say  "left".
            pet.say("left")
        # If the enemy on the right of the pet:
        else:
            # Say  "right".
            pet.say("right")
        pass
