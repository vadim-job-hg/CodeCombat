# https://codecombat.com/play/level/double-gaps

# Get the hero and the peasant to the south.

# The function move your hero down along the center line.
def moveDownCenter():
    x = 40
    y = hero.pos.y - 12
    hero.moveXY(x, y)

# The function build a fence on the right of something.
def buildRightOf(something):
    # buildXY a "fence" 20 meters to something's right.
    x = something.pos.x + 20
    y = something.pos.y
    hero.buildXY("fence", x, y)

# The function build a fence on the left of something.
def buildLeftOf(something):
    # buildXY a "fence" 20 meters to something's left.
    x = something.pos.x - 20
    y = something.pos.y
    hero.buildXY("fence", x, y)

while True:
    ogre = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    if ogre:
        buildLeftOf(ogre)
    if coin:
        buildRightOf(coin)
    moveDownCenter()
