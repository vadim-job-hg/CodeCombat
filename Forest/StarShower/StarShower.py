# https://codecombat.com/play/level/star-shower
# A star shower is a time when gems and coins appear around you.
# Metal coins disappear quickly, run for them only they are close (< 20m).
# Gems don't disappear, run for them every time when you see them.

while True:
    pass
    # Find the nearest item.
    item = hero.findNearestItem()
    # Find the distance between the hero and the item.
    if item:
        distance = hero.distanceTo(item)
        # If the item's type is 'gem' OR the distance to the item less than 20 metres:
        if item.type == 'gem' or distance < 20:
            # Take it.
            hero.moveXY(item.pos.x, item.pos.y)

