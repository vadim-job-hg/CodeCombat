# https://codecombat.com/play/level/bone-dance
# Just don't angry skeletons for 60 seconds.

# This function is useful to compare float numbers.
def almostEqual(a, b):
    return Math.abs(a - b) < 1

while True:
    skeleton = hero.findNearestEnemy()
    # Find the radius of the skeleton circle.
    radius = hero.distanceTo(skeleton)
    # If the length of the circle is almost equal 100:
    length = 2*radius*Math.PI
    if almostEqual(length, 100):
        # Say, Sing, Shout anything (one time).
        hero.say('ALARM!')


