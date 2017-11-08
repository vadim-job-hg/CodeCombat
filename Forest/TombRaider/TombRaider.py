# https://codecombat.com/play/level/tomb-raider
# A forgotten tomb in the forest!
# But the ogres are hot on your heels.
# Break open the tomb, while defending yourself from the munchkins.

# This function should attack an enemy if it exists, otherwise attack the door!
def checkToDefend(target):
    # Check if the target exists
    if target:
        # If so, attack the target
        hero.attack(target)
    # Use an else to do something if there is no target
    else:
        # Otherwise attack the "Door"
        hero.attack("Door")
    pass


while True:
    enemy = hero.findNearestEnemy()
    checkToDefend(enemy)
