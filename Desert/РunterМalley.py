# https://codecombat.com/play/level/hunter-valley

# Escape to the right side of the valley.

# The function moves the hero to down and right.
def moveDownRight(step):
    hero.moveXY(hero.pos.x + step, hero.pos.y - step)

# The function moves the hero to up and right.
def moveUpRight(step):
    # Complete this function:
    hero.moveXY(hero.pos.x + step, hero.pos.y + step)
    pass

# The hunter is kind and will show the route.
hunter = hero.findFriends()[0]
route = hunter.route
routeIndex = 0

while routeIndex < len(route):
    direction = route[routeIndex]
    if direction > 0:
        moveUpRight(8)
    else:
        # Use a function moveDownRight with the shift 8:
        moveDownRight(8)
        pass
    routeIndex += 1
