# https://codecombat.com/play/level/danger-picklock
# You need to break the door.

# The function checks the equality with 5% inaccuracy.
def almostEqual(a, b):
    return Math.abs(a - b) < (b * 0.05)

# We have a bomb for the door, but it's weak.
bomb = hero.findByType("robobomb")[0]
# Wizards can charge the bomb.
wizards = hero.findByType("wizard")
# The area of a circle should be equal:
chargeArea = bomb.chargeArea
while True:
    # Circle radius:
    radius = bomb.distanceTo(wizards[0])
    # Find the current area of the circle.
    area = radius*radius*Math.PI
    # If it's almost equal to chargeArea:
    if(almostEqual(chargeArea, area)):
        # Say something: 
        hero.say('Run, Forest, Run')

