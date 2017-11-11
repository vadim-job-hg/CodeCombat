# https://codecombat.com/play/level/dangerous-tracks
# Protect the village with fire traps.
# Mine all passages in four directions.
# You have 80 seconds before ogre attack.

# Build traps on the line y=114 from x=40 to x=112 with step=24.
def buildNorthLine():
    for x in range(40, 113, 24):
        hero.buildXY("fire-trap", x, 114)


# Build traps on the line x=140 from y=110 to y=38 with step=18.
def buildEastLine():
    for y in range(110, 37, -18):
        hero.buildXY("fire-trap", 140, y)
    pass


# Build traps on the line y=22 from x=132 to x=32 with step=20.
def buildSouthLine():
    for x in range(132, 31, -20):
        hero.buildXY("fire-trap", x, 22)
        # Complete this function:


# Build traps on the line x=20 from y=28 to y=108 with step=16.
def buildWestLine():
    for y in range(28, 109, 16):
        hero.buildXY("fire-trap", 20, y)
    # Complete this function:
    pass


buildNorthLine();
buildEastLine();
buildSouthLine();
buildWestLine();
hero.moveXY(40, 94);
