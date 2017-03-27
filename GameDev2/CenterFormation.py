# https://codecombat.com/play/level/center-formation
# Night is coming! Move all the soldiers towards the fire.

def centerFormation(event):
    # The event's target is any given soldier.
    unit = event.target
    # Now move the unit (a soldier) towards the center fire.
    unit.moveXY(40, 37)

# This spawns the four soldiers:
game.spawnXY("soldier", 16, 57)
game.spawnXY("soldier", 15, 13)
game.spawnXY("soldier", 63, 13)
game.spawnXY("soldier", 67, 57)

# This sets the soldier's spawn action to the function centerFormation:
game.setActionFor("soldier", "spawn", centerFormation)
