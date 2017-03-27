# https://codecombat.com/play/level/white-rabbit
# Follow by the lightstone and escape from the room.

while True:
    item = hero.findNearestItem()
    if item:
        pass
        # Get the item's position with the property "pos".
        pos = item.pos
        # Get "x" and "y" coordinates from the position.
        x = pos.x
        y = pos.y
        # Move to the coordinates (x, y).
        hero.moveXY(x, y)
