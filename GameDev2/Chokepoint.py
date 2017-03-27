# https://codecombat.com/play/level/chokepoint
# Ogres are advancing through the forest lanes!
# Spawn some soldiers and have them defend their lanes!

def defendLane(event):
    # Remember to create a variable for the target, to remember:
    unit = event.target
    startX = unit.pos.x
    while True:
        enemy = unit.findNearestEnemy()
        # If the unit can see an enemy, attack the enemy:
        if enemy:
            # Else, move the unit back to it's starting x and y.
            unit.attack(enemy)
        else:
            unit.moveXY(startX, 16)


game.spawnXY("soldier", 9, 16)
game.spawnXY("soldier", 30, 16)
game.spawnXY("soldier", 54, 16)
game.spawnXY("soldier", 75, 16)

game.setActionFor("soldier", "spawn", defendLane)
