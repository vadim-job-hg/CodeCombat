# https://codecombat.com/play/level/coincrumbs
# Follow by the coin trail and escape from the room.

while True:
    # Find the nearest item.
    item = hero.findNearestItem()
    if item:
        # Get the position of the item.
        itemPosition = item.pos
        # Get X and Y coordinates of the item.
        itemX = itemPosition.x
        itemY = itemPosition.y
        # To collect the item, move to the item.
        hero.moveXY(itemX, itemY)
