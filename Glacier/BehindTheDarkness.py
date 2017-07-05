# https://codecombat.com/play/level/behind-the-darkness
# Survive 70 seconds.

# The function allows you to wait for an ability.
def waitForAndAttack(abilityName):
    while True:
        if hero.isReady(abilityName):
            break
        enemy = hero.findNearestEnemy()
        if enemy and enemy.type != "yeti" and hero.distanceTo(enemy) < 15:
            hero.attack(enemy)
SE = {"x": 52, "y": 20}
NE = {"x": 52, "y": 48}
NW = {"x": 28, "y": 48}
SW = {"x": 28, "y": 20}
# Summon the Wall of Darkness to protect yourself.
# First, the east, north, and west sides.
# The order is important!
hero.wallOfDarkness([SW, NW, NE, SE])
# Wait for "wall-of-darkness" and attack incoming ogres.
waitForAndAttack("wall-of-darkness")
# Second, summon the wall to the east and south sides:
hero.wallOfDarkness([NE, SE, SW])
# Wait for "wall-of-darkness" and attack incoming ogres.
waitForAndAttack("wall-of-darkness")
# Third, the north and west sides:
hero.wallOfDarkness([NE, NW, SW])
# Wait for "wall-of-darkness" and attack incoming ogres.
waitForAndAttack("wall-of-darkness")