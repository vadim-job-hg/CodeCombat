# http://codecombat.com/play/level/square-shield
# Incoming yeti attack!
# Use your paladins to form a square!
# Command Illumina and Vaelia to move to the corners of the square.

def findByName(name, thangs):
    for i in range(len(thangs)):
        thang = thangs[i]
        if thang.id == name:
            return thang
    return None


friends = hero.findFriends()
celadia = findByName("Celadia", friends)
dedalia = findByName("Dedalia", friends)

sideLength = celadia.distanceTo(dedalia)

# First find the remaining paladins and assign them to variables:
illumina = findByName("Illumina", friends)
vaelia = findByName("Vaelia", friends)
# Command both to move to the corners of the square.
# Remember squares have equal-length sides!
hero.command(illumina, 'move', {'x': celadia.pos.x, 'y': celadia.pos.y - sideLength})
hero.command(vaelia, 'move', {'x': dedalia.pos.x, 'y': dedalia.pos.y - sideLength})
